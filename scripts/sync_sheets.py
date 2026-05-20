#!/usr/bin/env python3
"""sync_sheets.py - dearmanga.com 記事一覧をGoogleスプレッドシートに同期"""
import os
import re
import glob
import gspread
from google.oauth2.service_account import Credentials

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
ARTICLES_DIR = os.path.join(PROJECT_ROOT, 'src', 'content', 'articles')

CREDS_FILE = '/Users/yushi/Documents/ms-contents/portal_scripts/google_credentials.json'
SHEET_ID = os.environ.get('DEARMANGA_SHEET_ID', '1n2XORLf0mNAk94wg5dpKI-gJHWUZf-os7C84PYBnVXQ')

SITE_URL = 'https://www.dearmanga.com'


def get_sheet():
    scopes = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]
    creds = Credentials.from_service_account_file(CREDS_FILE, scopes=scopes)
    gc = gspread.authorize(creds)
    return gc.open_by_key(SHEET_ID)


def get_or_create_ws(sh, title, rows=2000, cols=15):
    try:
        return sh.worksheet(title)
    except Exception:
        return sh.add_worksheet(title, rows=rows, cols=cols)


def get_field(content, key):
    m = re.search(rf'^{re.escape(key)}:\s*"?([^"\n]+)"?', content, re.MULTILINE)
    return m.group(1).strip().strip('"') if m else ''


def get_list_field(content, key):
    m = re.search(rf'^{re.escape(key)}:\n((?:  - .*\n?)+)', content, re.MULTILINE)
    if not m:
        return ''
    items = re.findall(r'  - "?([^"\n]+)"?', m.group(1))
    return ', '.join(items)


def get_git_added_date(filepath):
    """ファイルが最初にgit addされた日付を返す（YYYY-MM-DD）"""
    import subprocess
    try:
        result = subprocess.run(
            ['git', 'log', '--follow', '--format=%as', '--diff-filter=A', '--', filepath],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )
        date = result.stdout.strip().splitlines()
        return date[-1] if date else ''
    except Exception:
        return ''


def get_git_tracked_covers():
    import subprocess
    result = subprocess.run(
        ['git', 'ls-files', 'public/covers/'],
        capture_output=True, text=True, cwd=PROJECT_ROOT
    )
    return {os.path.basename(f).replace('.jpg', '') for f in result.stdout.splitlines()}


def collect_articles():
    tracked_covers = get_git_tracked_covers()
    articles = []
    pattern = os.path.join(ARTICLES_DIR, '**', '*.md')
    for filepath in sorted(glob.glob(pattern, recursive=True)):
        genre_dir = os.path.basename(os.path.dirname(filepath))
        slug = os.path.basename(filepath).replace('.md', '')
        with open(filepath, encoding='utf-8') as f:
            content = f.read()
        url = f"{SITE_URL}/{genre_dir}/{slug}"
        articles.append({
            'mangaTitle':    get_field(content, 'mangaTitle'),
            'mangaTitleJa':  get_field(content, 'mangaTitleJa'),
            'mangaAuthor':   get_field(content, 'mangaAuthor'),
            'genre':       get_field(content, 'genre'),
            'genreSlug':   get_field(content, 'genreSlug') or genre_dir,
            'slug':        slug,
            'url':         url,
            'rating':      get_field(content, 'rating'),
            'publishedAt': get_field(content, 'publishedAt'),
            'addedAt':     get_git_added_date(filepath),
            'tags':        get_list_field(content, 'tags'),
            'hasCover':    '○' if slug in tracked_covers else '×',
            'englishStatus': get_field(content, 'englishStatus'),
            'read':        '○' if re.search(r'^read:\s*true', content, re.MULTILINE) else '',
            'noindex':     '○' if re.search(r'^noindex:\s*true', content, re.MULTILINE) else '',
            'effectiveIndex': ('○' if re.search(r'^read:\s*true', content, re.MULTILINE)
                              and not re.search(r'^noindex:\s*true', content, re.MULTILINE)
                              else '×'),
            'rewritten':   (lambda m: m.group(1).strip('"') if m else '')(re.search(r'^rewritten:\s*"?([^"\n]+)"?', content, re.MULTILINE)),
        })
    return articles


def main():
    if not SHEET_ID:
        print('ERROR: SHEET_ID が設定されていません。')
        print('  スクリプト内の SHEET_ID を書き換えるか、')
        print('  DEARMANGA_SHEET_ID=xxxx python3 sync_sheets.py で実行してください。')
        return

    articles = collect_articles()

    sh = get_sheet()
    headers = ['マンガタイトル', '日本語タイトル', '著者', 'ジャンル', 'ジャンルSlug', 'Slug', 'URL',
               '評価', '公開日', '追加日', 'タグ', '画像', '英語版',
               'Read', 'Noindex', 'インデックス対象', 'リライト済']
    rows = [headers]
    for a in articles:
        rows.append([
            a['mangaTitle'],
            a['mangaTitleJa'],
            a['mangaAuthor'],
            a['genre'],
            a['genreSlug'],
            a['slug'],
            a['url'],
            str(a['rating']),
            str(a['publishedAt']),
            str(a['addedAt']),
            a['tags'],
            a['hasCover'],
            a['englishStatus'],
            a['read'],
            a['noindex'],
            a['effectiveIndex'],
            a['rewritten'],
        ])

    ws = get_or_create_ws(sh, '記事一覧', rows=max(len(rows) + 100, 2000), cols=max(len(headers), 17))
    ws.clear()
    ws.update(rows, 'A1', value_input_option='USER_ENTERED')

    print(f'OK: {len(rows) - 1}件の記事を書き込みました')


if __name__ == '__main__':
    main()
