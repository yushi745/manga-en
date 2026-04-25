#!/usr/bin/env python3
"""
ASIN検証スクリプト
Open Library APIで全記事のASINを照合し、怪しいものをリストアップする。

使い方:
  python3 scripts/verify_asins.py
  → scripts/asin_issues.csv に問題リストを出力

対応状況:
  OK        - Open LibraryでASINと一致するISBNを確認済み
  MISMATCH  - Open LibraryにISBNあるが現在のASINと不一致 → 要修正
  NOT_FOUND - Open Libraryで作品が見つからない → 手動確認推奨
"""

import os, re, glob, json, time, urllib.request, urllib.parse, csv

ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")
OUTPUT_CSV = os.path.expanduser("~/Documents/manga-en/scripts/asin_issues.csv")

def extract_frontmatter(path):
    content = open(path).read()
    m = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split('\n'):
        kv = re.match(r'^(\w+):\s*"?([^"#\n]*)"?', line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip('"')
    return fm

def search_openlibrary(title, author="", delay=1.2):
    time.sleep(delay)
    query = f"{title} {author}".strip()
    url = f"https://openlibrary.org/search.json?q={urllib.parse.quote(query)}&limit=5"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "manga-en-verifier/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        results = []
        for doc in data.get('docs', []):
            isbns = doc.get('isbn', [])
            isbn10 = [i for i in isbns if len(i) == 10]
            isbn13 = [i for i in isbns if len(i) == 13]
            results.append({
                'title': doc.get('title', ''),
                'isbn10': isbn10[:5],
                'isbn13': isbn13[:3],
            })
        return results
    except Exception as e:
        return []

def check_asin(asin, ol_results):
    for r in ol_results:
        if asin in r['isbn10']:
            return 'OK'
    return 'MISMATCH'

def get_suggested_isbn(ol_results):
    for r in ol_results:
        if r['isbn10']:
            return r['isbn10'][0]
    return ''

files = sorted(glob.glob(f"{ARTICLES_DIR}/**/*.md", recursive=True))
print(f"Total articles: {len(files)}\n")

issues = []
ok_count = 0
skip_count = 0

for i, fp in enumerate(files):
    fm = extract_frontmatter(fp)
    asin = fm.get('amazonASIN', '').strip()
    title = fm.get('mangaTitle', '').strip()
    author = fm.get('mangaAuthor', '').strip().split('/')[0].strip()
    slug = fm.get('slug', os.path.basename(fp).replace('.md', ''))

    if not asin or not title:
        skip_count += 1
        continue

    results = search_openlibrary(title, author)

    if not results:
        status = 'NOT_FOUND'
        suggested = ''
        ol_title = ''
    else:
        status = check_asin(asin, results)
        suggested = get_suggested_isbn(results)
        ol_title = results[0]['title']

    if status == 'OK':
        ok_count += 1
        if (i + 1) % 100 == 0:
            print(f"[{i+1}/{len(files)}] {ok_count} OK so far...")
    else:
        issues.append({
            'slug': slug,
            'mangaTitle': title,
            'current_asin': asin,
            'status': status,
            'ol_first_title': ol_title,
            'suggested_isbn10': suggested,
        })
        print(f"[{i+1}/{len(files)}] {status:12s} {slug}  current={asin}  suggested={suggested}")

print(f"\n=== DONE ===")
print(f"OK: {ok_count} | Issues: {len(issues)} | Skipped (no ASIN/title): {skip_count}")
print(f"  MISMATCH: {sum(1 for x in issues if x['status']=='MISMATCH')}")
print(f"  NOT_FOUND: {sum(1 for x in issues if x['status']=='NOT_FOUND')}")

with open(OUTPUT_CSV, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['slug', 'mangaTitle', 'current_asin', 'status', 'ol_first_title', 'suggested_isbn10'])
    writer.writeheader()
    writer.writerows(issues)

print(f"\nIssues saved to: {OUTPUT_CSV}")
