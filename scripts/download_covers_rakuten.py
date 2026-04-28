#!/usr/bin/env python3
"""
楽天ブックスAPIを使って全記事のカバー画像を再ダウンロードするスクリプト。
mangaTitleJa（日本語タイトル）があればそれを優先、なければ mangaTitle で検索。
楽天で見つからない場合は Google Books APIで補完。
"""
import os, re, glob, json, time, urllib.request, urllib.parse

ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")
COVERS_DIR = os.path.expanduser("~/Documents/manga-en/public/covers")
RAKUTEN_API_URL = 'https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404'
SITE_URL = 'https://www.dearmanga.com'

def load_env():
    env_path = os.path.expanduser("~/Documents/manga-en/.env.local")
    env = {}
    for line in open(env_path):
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

def write_cover_image(fp, content, slug):
    """frontmatter に coverImage がなければ slug: の直後に追加する"""
    if 'coverImage:' in content:
        return
    cover_line = 'coverImage: "/covers/' + slug + '.jpg"'
    new_content = re.sub(
        r'(^slug:.*$)',
        r'\1\n' + cover_line,
        content,
        count=1,
        flags=re.MULTILINE,
    )
    if new_content != content:
        open(fp, 'w', encoding='utf-8').write(new_content)

def rakuten_search(title):
    params = urllib.parse.urlencode({
        'applicationId': APP_ID,
        'accessKey': ACCESS_KEY,
        'format': 'json',
        'title': title,
        'booksGenreId': '001001',  # コミック
        'hits': 5,
        'sort': 'sales',
    })
    url = f'{RAKUTEN_API_URL}?{params}'
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0',
        'Origin': SITE_URL,
        'Referer': SITE_URL + '/',
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        for wrapper in data.get('Items', []):
            item = wrapper.get('Item', wrapper)
            img = item.get('largeImageUrl', '')
            found_title = item.get('title', '')
            if img and 'noimage' not in img:
                # _ex=200x200 → _ex=600x600 に差し替えてより大きい画像を取得
                img = img.replace('_ex=200x200', '_ex=600x600')
                return img, found_title
        return None, None
    except Exception as e:
        print(f'    Rakuten ERR: {e}')
        return None, None

def google_books_search(query):
    params = urllib.parse.urlencode({
        'q': f'intitle:{query}',
        'langRestrict': 'ja',
        'maxResults': 5,
        'printType': 'books',
    })
    url = f'https://www.googleapis.com/books/v1/volumes?{params}'
    req = urllib.request.Request(url, headers={'User-Agent': 'manga-en/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        for item in data.get('items', []):
            info = item['volumeInfo']
            thumb = info.get('imageLinks', {}).get('thumbnail', '')
            if thumb:
                thumb = thumb.replace('zoom=1', 'zoom=3').replace('http://', 'https://')
                return thumb, info.get('title', '')
        return None, None
    except Exception as e:
        print(f'    Google Books ERR: {e}')
        return None, None

def download_image(url, dest):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
        if len(data) < 5000:
            return False, len(data)
        open(dest, 'wb').write(data)
        return True, len(data)
    except Exception as e:
        print(f'    Download ERR: {e}')
        return False, 0

files = sorted(glob.glob(f"{ARTICLES_DIR}/**/*.md", recursive=True))
print(f"対象ファイル: {len(files)} 件\n")

ok_rakuten, ok_google, fail_count = 0, 0, 0
failed_list = []

for i, fp in enumerate(files, 1):
    content = open(fp, encoding='utf-8').read()
    slug = get_field(content, 'slug') or os.path.basename(fp).replace('.md', '')
    manga_title_ja = get_field(content, 'mangaTitleJa')
    manga_title = get_field(content, 'mangaTitle')
    dest = f"{COVERS_DIR}/{slug}.jpg"

    search_title = manga_title_ja or manga_title
    if not search_title:
        print(f"[{i}/{len(files)}] {slug}: タイトル不明 → SKIP")
        fail_count += 1
        failed_list.append((slug, ''))
        continue

    print(f"[{i}/{len(files)}] {slug} | {search_title} ...", end=' ', flush=True)
    time.sleep(1.0)

    # 楽天API（主）
    img_url, found_title = rakuten_search(search_title)
    if not img_url and manga_title_ja and manga_title:
        time.sleep(0.5)
        img_url, found_title = rakuten_search(manga_title)

    if img_url:
        ok, size = download_image(img_url, dest)
        if ok:
            print(f"楽天OK ({size//1024}KB) ← {found_title}")
            write_cover_image(fp, content, slug)
            ok_rakuten += 1
            continue

    # Google Books（補助）
    time.sleep(0.5)
    img_url, found_title = google_books_search(search_title)
    if img_url:
        ok, size = download_image(img_url, dest)
        if ok:
            print(f"GoogleOK ({size//1024}KB) ← {found_title}")
            write_cover_image(fp, content, slug)
            ok_google += 1
            continue

    print(f"NOT FOUND")
    fail_count += 1
    failed_list.append((slug, search_title))

print(f"\n=== 完了 ===")
print(f"楽天成功: {ok_rakuten} / Google補完: {ok_google} / 失敗: {fail_count}")
if failed_list:
    print("失敗リスト:")
    for slug, title in failed_list:
        print(f"  [{slug}] {title}")
