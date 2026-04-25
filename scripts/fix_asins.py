#!/usr/bin/env python3
"""
ASIN一括修正スクリプト
verify_asins.py が出力した asin_issues.csv の MISMATCH 行を自動修正する。

使い方:
  # まず verify_asins.py を実行してCSVを生成
  python3 scripts/verify_asins.py

  # CSVを確認・編集（suggested_isbn10 が正しいか目視チェック推奨）

  # MISMATCHのみ自動修正（suggested_isbn10 が空でない行）
  python3 scripts/fix_asins.py

  # dry-run（変更内容を確認するだけ）
  python3 scripts/fix_asins.py --dry-run
"""

import os, re, glob, csv, sys

ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")
INPUT_CSV = os.path.expanduser("~/Documents/manga-en/scripts/asin_issues.csv")

dry_run = "--dry-run" in sys.argv

def find_article(slug):
    matches = glob.glob(f"{ARTICLES_DIR}/**/{slug}.md", recursive=True)
    return matches[0] if matches else None

def fix_asin(path, new_asin):
    content = open(path).read()
    new_content = re.sub(
        r'^(amazonASIN:\s*)"[^"]*"',
        f'\\1"{new_asin}"',
        content,
        flags=re.MULTILINE
    )
    if new_content == content:
        return False
    if not dry_run:
        open(path, 'w').write(new_content)
    return True

fixed = 0
skipped = 0

with open(INPUT_CSV) as f:
    rows = list(csv.DictReader(f))

mismatch_rows = [r for r in rows if r['status'] == 'MISMATCH' and r['suggested_isbn10']]
print(f"MISMATCH with suggested ISBN: {len(mismatch_rows)}")
print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}\n")

for row in mismatch_rows:
    slug = row['slug']
    old_asin = row['current_asin']
    new_asin = row['suggested_isbn10']
    path = find_article(slug)

    if not path:
        print(f"  NOT FOUND: {slug}")
        skipped += 1
        continue

    ok = fix_asin(path, new_asin)
    if ok:
        print(f"  {'[DRY] ' if dry_run else ''}FIXED: {slug}  {old_asin} → {new_asin}")
        fixed += 1
    else:
        print(f"  SKIP (no change): {slug}")
        skipped += 1

print(f"\nFixed: {fixed} | Skipped: {skipped}")
if dry_run:
    print("(dry-run — no files modified)")
