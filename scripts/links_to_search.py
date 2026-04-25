#!/usr/bin/env python3
"""
全記事のAmazon /dp/<ASIN> リンクを検索URLに一括変換。

変換前: https://www.amazon.com/dp/1646517849
変換後: https://www.amazon.com/s?k=Ya+Boy+Kongming%21+manga

使い方:
  python3 scripts/links_to_search.py           # dry-run（変更なし・確認のみ）
  python3 scripts/links_to_search.py --apply   # 実際に書き換え
"""

import os, re, glob, sys, urllib.parse

ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")
APPLY = "--apply" in sys.argv

# frontmatterからmangaTitleを取得
def get_manga_title(content):
    m = re.search(r'^mangaTitle:\s*"([^"]+)"', content, re.MULTILINE)
    return m.group(1) if m else None

# /dp/ASIN リンクを検索URLに変換
def make_search_url(title):
    q = urllib.parse.quote_plus(f"{title} manga")
    return f"https://www.amazon.com/s?k={q}"

files = sorted(glob.glob(f"{ARTICLES_DIR}/**/*.md", recursive=True))
changed = 0
skipped = 0

for fp in files:
    content = open(fp).read()
    title = get_manga_title(content)
    if not title:
        skipped += 1
        continue

    # Amazon /dp/ リンクを検索URLに置換
    search_url = make_search_url(title)
    new_content = re.sub(
        r'https://www\.amazon\.com/dp/[A-Z0-9]+',
        search_url,
        content
    )

    if new_content == content:
        skipped += 1
        continue

    slug = os.path.basename(fp).replace('.md', '')
    count = len(re.findall(r'https://www\.amazon\.com/dp/[A-Z0-9]+', content))
    print(f"{'APPLY' if APPLY else 'DRY  '} | {slug:45s} | {count} link(s) → {search_url}")

    if APPLY:
        open(fp, 'w').write(new_content)
    changed += 1

print(f"\n{'Applied' if APPLY else 'Would change'}: {changed} files | Skipped: {skipped}")
