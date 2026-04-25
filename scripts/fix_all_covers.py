#!/usr/bin/env python3
"""
全記事のカバー画像を修正する。
- 既存ファイルを無条件上書き（スキップなし）
- タイトル類似チェックで間違い画像を弾く
- 楽天API → Google Books → Amazon CDN の順でフォールバック
"""
import os, re, glob, json, time, urllib.request, urllib.parse

ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")
COVERS_DIR = os.path.expanduser("~/Documents/manga-en/public/covers")
RAKUTEN_API_URL = 'https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404'
SITE_URL = 'https://www.dearmanga.com'

def load_env():
    env = {}
    for line in open(os.path.expanduser("~/Documents/manga-en/.env.local")):
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip()
    return env

env = load_env()
APP_ID = env.get('RAKUTEN_APP_ID', '')
ACCESS_KEY = env.get('RAKUTEN_ACCESS_KEY', '')
if not APP_ID or not ACCESS_KEY:
    print("ERROR: RAKUTEN_APP_ID / RAKUTEN_ACCESS_KEY が .env.local にありません")
    exit(1)

def get_field(content, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    return m.group(1).strip().strip('"') if m else None

def normalize(s):
    """タイトル比較用の正規化: 小文字化、記号除去、空白統一"""
    s = s.lower()
    # 全角→半角
    s = s.replace('　', ' ')
    # 巻数表記を除去: （1）(1) vol.1 #1 など
    s = re.sub(r'[（(]\d+[）)]', '', s)
    s = re.sub(r'[\s\-_]+', ' ', s)
    s = s.strip()
    return s

def titles_match(search_query, found_title):
    """
    検索クエリと見つかったタイトルが類似しているか判定。
    CJKタイトルはスペースがないので文字数比較で判定する。
    """
    sq = normalize(search_query)
    ft = normalize(found_title)

    # 完全一致
    if sq == ft:
        return True

    has_cjk = any('　' <= c <= '鿿' or '가' <= c <= '힯' for c in sq)

    if has_cjk:
        sq_chars = re.sub(r'\s', '', sq)
        ft_chars = re.sub(r'\s', '', ft)

        # ft が sq を含むか（ft が sq の部分集合）→ OK
        if ft_chars in sq_chars:
            return True

        # sq が ft の先頭に一致する場合: 直後の文字で判定
        if ft_chars.startswith(sq_chars):
            rest = ft_chars[len(sq_chars):]
            # 日本語助詞（の・が・を・に・は・も・で・と・へ・や）が続くと別の作品
            jp_particles = 'のがをにはもでとへや'
            if rest and rest[0] in jp_particles:
                return False
            return True

        # sq が ft に完全一致しない場合: CJK文字数の比率チェック
        def cjk_len(s):
            return len(re.sub(r'[^　-鿿가-힯]', '', s))

        sq_cjk_len = cjk_len(sq_chars)
        ft_cjk_len = cjk_len(ft_chars)

        # ft のCJK部分が sq より50%以上長ければ別の作品（サブタイトルではなく独立した別作品）
        if ft_cjk_len > sq_cjk_len * 1.5 and sq_cjk_len > 1:
            return False

        # sq が ft のどこかに含まれる
        if sq_chars in ft_chars:
            return True

        # 先頭文字類似度
        common = sum(1 for a, b in zip(sq_chars, ft_chars) if a == b)
        return common / max(len(sq_chars), 1) >= 0.7

    # 英語: 単語分割マッチ
    # ft が sq に含まれる → OK
    if ft in sq:
        return True
    # sq が ft より20%以上短ければ別の作品の可能性
    words = [w for w in sq.split() if len(w) >= 2]
    if not words:
        return True
    matches = sum(1 for w in words if w in ft)
    return matches / len(words) >= 0.6

def rakuten_search(title):
    params = urllib.parse.urlencode({
        'applicationId': APP_ID, 'accessKey': ACCESS_KEY,
        'format': 'json', 'title': title, 'booksGenreId': '001001',
        'hits': 10, 'sort': 'sales',
    })
    req = urllib.request.Request(f'{RAKUTEN_API_URL}?{params}', headers={
        'User-Agent': 'Mozilla/5.0', 'Origin': SITE_URL, 'Referer': SITE_URL + '/',
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        for wrapper in data.get('Items', []):
            item = wrapper.get('Item', wrapper)
            img = item.get('largeImageUrl', '')
            found = item.get('title', '')
            if img and 'noimage' not in img and titles_match(title, found):
                img = img.replace('_ex=200x200', '_ex=600x600')
                return img, found
        # 類似チェックで全部落ちた場合、件数を報告
        total = len(data.get('Items', []))
        if total > 0:
            candidates = [w.get('Item', w).get('title','') for w in data.get('Items', [])]
            return None, f"NOMATCH({total}件: {candidates[:2]})"
        return None, "NORESULT"
    except Exception as e:
        return None, f"ERR:{e}"

def google_search(query, title_hint):
    params = urllib.parse.urlencode({
        'q': query, 'langRestrict': 'ja', 'maxResults': 10, 'printType': 'books',
    })
    req = urllib.request.Request(
        f'https://www.googleapis.com/books/v1/volumes?{params}',
        headers={'User-Agent': 'manga-en/1.0'}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        for item in data.get('items', []):
            info = item['volumeInfo']
            found = info.get('title', '')
            thumb = info.get('imageLinks', {}).get('thumbnail', '')
            if thumb and titles_match(title_hint, found):
                thumb = thumb.replace('zoom=1', 'zoom=3').replace('http://', 'https://')
                return thumb, found
        return None, "NOMATCH"
    except Exception as e:
        return None, f"ERR:{e}"

def amazon_cdn(asin):
    """ASINからAmazon CDN画像を取得（タイトル検証なし・最終手段）"""
    if not asin or len(asin) < 8:
        return None
    url = f"https://images-na.ssl-images-amazon.com/images/P/{asin}.01.LZZZZZZZ.jpg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        # GIFはプレースホルダー（43バイト程度）→ 拒否
        if len(data) > 8000 and data[:2] == b'\xff\xd8':
            return data
    except:
        pass
    return None

def save_image(url, dest):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) < 5000:
            return False, len(data), "too_small"
        # JPEG か PNG のみ受け付ける
        if data[:2] not in (b'\xff\xd8', b'\x89P'):
            return False, len(data), "not_jpeg"
        open(dest, 'wb').write(data)
        return True, len(data), ""
    except Exception as e:
        return False, 0, str(e)


# ---- メイン ----

files = sorted(glob.glob(f"{ARTICLES_DIR}/**/*.md", recursive=True))
total = len(files)
print(f"対象: {total} 件\n")

ok_rakuten = ok_google = ok_amazon = 0
fail_list = []
nomatch_list = []

for i, fp in enumerate(files, 1):
    content = open(fp, encoding='utf-8').read()
    slug = get_field(content, 'slug') or os.path.basename(fp).replace('.md', '')
    manga_title_ja = get_field(content, 'mangaTitleJa')
    manga_title    = get_field(content, 'mangaTitle')
    asin           = get_field(content, 'amazonASIN')
    dest = f"{COVERS_DIR}/{slug}.jpg"

    search_title = manga_title_ja or manga_title
    if not search_title:
        print(f"[{i}/{total}] {slug}: タイトル不明 SKIP")
        fail_list.append((slug, '', 'no_title'))
        continue

    print(f"[{i}/{total}] {slug} | {search_title}", end=' ... ', flush=True)
    time.sleep(0.8)

    # 1. 楽天API（mangaTitleJa）
    img_url, found = rakuten_search(search_title)

    # 1b. 楽天API（englishタイトルで再試行）
    if not img_url and manga_title_ja and manga_title and manga_title != manga_title_ja:
        time.sleep(0.3)
        img_url2, found2 = rakuten_search(manga_title)
        if img_url2:
            img_url, found = img_url2, found2

    if img_url:
        ok, size, err = save_image(img_url, dest)
        if ok and size > 15000:
            print(f"楽天OK({size//1024}KB)←{found}")
            ok_rakuten += 1
            continue
        elif ok:
            # 小さすぎる可能性 → Amazonも試す
            pass

    # 2. Google Books
    time.sleep(0.3)
    g_query = f"intitle:{search_title} manga"
    g_url, g_found = google_search(g_query, search_title)
    if g_url:
        ok, size, err = save_image(g_url, dest)
        if ok and size > 5000:
            print(f"Google({size//1024}KB)←{g_found}")
            ok_google += 1
            continue

    # 3. Amazon CDN（ASIN直接）
    if asin:
        data = amazon_cdn(asin)
        if data:
            open(dest, 'wb').write(data)
            print(f"Amazon({len(data)//1024}KB)[ASIN:{asin}]")
            ok_amazon += 1
            continue

    # 全部失敗
    reason = found if 'ERR' in str(found) or 'NOMATCH' in str(found) else 'all_failed'
    if 'NOMATCH' in str(found):
        nomatch_list.append((slug, search_title, found))
    else:
        fail_list.append((slug, search_title, reason))
    print(f"FAIL({reason})")

# ---- 結果サマリー ----
print(f"\n{'='*60}")
print(f"完了: 楽天{ok_rakuten} / Google{ok_google} / Amazon{ok_amazon}")
print(f"失敗: {len(fail_list)} / タイトル不一致: {len(nomatch_list)}")

if nomatch_list:
    print(f"\n=== タイトル不一致（Amazonフォールバックも失敗） ===")
    for slug, title, reason in nomatch_list[:30]:
        print(f"  [{slug}] {title}: {reason}")

if fail_list:
    print(f"\n=== 完全失敗 ===")
    for slug, title, reason in fail_list[:30]:
        print(f"  [{slug}] {title}: {reason}")

# 結果をファイルに保存
with open('/tmp/cover_fix_results.txt', 'w') as f:
    f.write(f"楽天:{ok_rakuten} Google:{ok_google} Amazon:{ok_amazon}\n")
    f.write(f"失敗:{len(fail_list)} NOMATCH:{len(nomatch_list)}\n\n")
    for slug, title, reason in fail_list + nomatch_list:
        f.write(f"FAIL [{slug}] {title}: {reason}\n")
print(f"\n結果 → /tmp/cover_fix_results.txt")
