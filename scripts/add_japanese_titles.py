#!/usr/bin/env python3
"""
Jikan API (MyAnimeList) を使って全記事に mangaTitleJa を追加するスクリプト。
既に mangaTitleJa がある記事はスキップ。
"""
import os, re, glob, json, time, urllib.request, urllib.parse

ARTICLES_DIR = os.path.expanduser("~/Documents/manga-en/src/content/articles")

def get_frontmatter_raw(content):
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return None, None, None
    return m.group(0), m.group(1), m.end()

def get_field(fm_text, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]+)"?', fm_text, re.MULTILINE)
    return m.group(1).strip().strip('"') if m else None

def jikan_search(title):
    query = urllib.parse.quote(title)
    url = f"https://api.jikan.moe/v4/manga?q={query}&limit=5&type=manga"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "manga-en/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read())
        entries = data.get('data', [])
        if not entries:
            return None
        # タイトルが最も近いものを選ぶ（英語タイトルが一致するもの優先）
        title_lower = title.lower()
        for entry in entries:
            en = (entry.get('title_english') or entry.get('title') or '').lower()
            ja = entry.get('title_japanese', '')
            if title_lower in en or en in title_lower:
                return ja if ja else None
        # 最初の結果の日本語タイトルを返す
        return entries[0].get('title_japanese') or None
    except Exception as e:
        print(f"    Jikan ERR: {e}")
        return None

files = sorted(glob.glob(f"{ARTICLES_DIR}/**/*.md", recursive=True))
print(f"対象ファイル: {len(files)} 件\n")

added, skipped, failed = [], [], []

for fp in files:
    content = open(fp, encoding='utf-8').read()
    fm_block, fm_text, fm_end = get_frontmatter_raw(content)
    if not fm_block:
        skipped.append(fp)
        continue

    # 既に mangaTitleJa がある場合はスキップ
    if 'mangaTitleJa:' in fm_text:
        skipped.append(fp)
        continue

    manga_title = get_field(fm_text, 'mangaTitle')
    slug = get_field(fm_text, 'slug') or os.path.basename(fp).replace('.md', '')

    if not manga_title:
        skipped.append(fp)
        continue

    print(f"[{slug}] {manga_title} ...", end=' ', flush=True)
    time.sleep(0.5)  # Jikan rate limit: 3req/s

    ja_title = jikan_search(manga_title)

    if not ja_title:
        print(f"FAIL")
        failed.append((slug, manga_title))
        continue

    print(f"→ {ja_title}")

    # mangaTitle の直後に mangaTitleJa を挿入
    new_fm = re.sub(
        r'(mangaTitle:\s*"[^"]*")',
        rf'\1\nmangaTitleJa: "{ja_title}"',
        fm_text
    )
    if new_fm == fm_text:
        # シングルクォートや引用符なしの場合も対応
        new_fm = re.sub(
            r'(mangaTitle:\s*[^\n]+)',
            rf'\1\nmangaTitleJa: "{ja_title}"',
            fm_text
        )

    new_content = content[:content.index('---')] + '---\n' + new_fm + '\n---' + content[fm_end:]
    open(fp, 'w', encoding='utf-8').write(new_content)
    added.append(slug)

print(f"\n=== 完了 ===")
print(f"追加: {len(added)} / スキップ: {len(skipped)} / 失敗: {len(failed)}")
if failed:
    print("失敗リスト（手動確認要）:")
    for slug, title in failed:
        print(f"  [{slug}] {title}")
