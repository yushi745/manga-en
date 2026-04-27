#!/usr/bin/env python3
"""
疑わしいカバー画像（20KB未満）をMangaDex APIで再取得するスクリプト。
"""
import os, re, glob, json, time, urllib.request, urllib.parse

COVERS_DIR = os.path.expanduser("~/Documents/manga-en/public/covers")
ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")
SIZE_THRESHOLD = 20000  # 20KB未満を対象

def get_frontmatter(path):
    content = open(path).read()
    m = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: return {}
    fm = {}
    for line in m.group(1).split('\n'):
        kv = re.match(r'^(\w+):\s*"?([^"#\n]*)"?', line)
        if kv: fm[kv.group(1)] = kv.group(2).strip().strip('"')
    return fm

def api(url, delay=3):
    time.sleep(delay)
    req = urllib.request.Request(url, headers={"User-Agent": "manga-en/1.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def download(url, dest, delay=1):
    time.sleep(delay)
    req = urllib.request.Request(url, headers={"User-Agent": "manga-en/1.0", "Referer": "https://mangadex.org"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    if len(data) < 10000:
        return False, len(data)
    open(dest, 'wb').write(data)
    return True, len(data)

def fix_cover(slug, manga_title):
    dest = f"{COVERS_DIR}/{slug}.jpg"
    # MangaDex検索
    for query in [manga_title, manga_title.split(':')[0].split('(')[0].strip()]:
        try:
            d = api(f"https://api.mangadex.org/manga?title={urllib.parse.quote(query)}&limit=5")
            if not d.get('data'): continue
            # タイトルが近いものを選ぶ
            for manga in d['data']:
                en_title = manga['attributes']['title'].get('en','') or list(manga['attributes']['title'].values())[0]
                manga_id = manga['id']
                # カバー取得
                cd = api(f"https://api.mangadex.org/cover?manga[]={manga_id}&limit=1")
                if not cd.get('data'): continue
                fn = cd['data'][0]['attributes']['fileName']
                img_url = f"https://uploads.mangadex.org/covers/{manga_id}/{fn}.256.jpg"
                ok, size = download(img_url, dest)
                if ok:
                    return True, size, en_title
        except Exception as e:
            print(f"    ERR: {e}")
            time.sleep(3)
    return False, 0, ""

# 対象スラッグを収集（20KB未満）
targets = []
for fp in sorted(glob.glob(f"{ARTICLES_DIR}/**/*.md", recursive=True)):
    fm = get_frontmatter(fp)
    slug = fm.get('slug', os.path.basename(fp).replace('.md',''))
    cover = f"{COVERS_DIR}/{slug}.jpg"
    if os.path.exists(cover) and os.path.getsize(cover) < SIZE_THRESHOLD:
        targets.append((slug, fm.get('mangaTitle', slug), os.path.getsize(cover)))

print(f"対象: {len(targets)} 件\n")

fixed, failed = [], []
for slug, title, old_size in targets:
    print(f"[{slug}] {title} ({old_size}B)")
    ok, new_size, found_title = fix_cover(slug, title)
    if ok:
        print(f"  OK → {new_size}B (found: {found_title})")
        fixed.append(slug)
    else:
        print(f"  FAIL")
        failed.append(slug)

print(f"\n=== 完了 ===")
print(f"修正成功: {len(fixed)} / 失敗: {len(failed)}")
if failed:
    print("失敗リスト:")
    for s in failed: print(f"  {s}")
