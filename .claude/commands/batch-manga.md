# /batch-manga

manga-enプロジェクトで漫画レビュー記事を3バッチ分（1バッチ=15記事、計45記事）生成・コミットするタスクを実行する。

## 実行ルール

- **必ず3バッチで終了**すること（それ以上も以下もダメ）
- **1バッチごと**に以下をチェックしてからgit commit:
  - 全15記事のfrontmatter（必須フィールド欠け・型ミスがないか）
  - 全15枚のカバー画像（5000バイト以上あるか）
  - スラッグ重複がないか（既存記事と被っていないか）
- **重大エラー**（カバー全滅・ファイル書き込み失敗・git commit失敗など）が出たら即停止してユーザーに報告
- コンパクションが発生しても**継続**すること（コンパクション後も3バッチ完了まで進める）
- 確認・報告なしで自律的に進める（軽微な失敗=カバー1〜2枚取得失敗は代替ISOBNで自己解決）

## バッチ番号の確認方法

```bash
git log --oneline | grep "batch" | head -5
```

最新のバッチ番号+1から開始する。

## 記事生成ルール

- `src/content/articles/<genreSlug>/<slug>.md` に保存
- カバー画像: `public/covers/<slug>.jpg`（MangaDex API → OpenLibrary fallback）
- publishedAt: バッチごとに1日ずつ増やす（前バッチの翌日）
- スラッグ重複チェック: `find src/content/articles -name "*.md" | sed 's|.*/||; s|\.md$||'`
- CLAUDE.mdの記事フォーマット（18セクション）を厳守
- 執筆者ペルソナ「Yu」で記述

## カバー取得スクリプト（Python）

```python
import urllib.request, json, os, time, urllib.parse

def fetch(url, timeout=10):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "manga-en/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except:
        return b""

def mangadex(title):
    q = urllib.parse.quote(title)
    data = fetch(f"https://api.mangadex.org/manga?title={q}&limit=5")
    if not data: return None
    j = json.loads(data)
    if not j.get("data"): return None
    uuid = j["data"][0]["id"]
    time.sleep(0.5)
    cdata = fetch(f"https://api.mangadex.org/cover?manga[]={uuid}&order[volume]=asc&limit=1")
    if not cdata: return None
    cj = json.loads(cdata)
    if not cj.get("data"): return None
    fn = cj["data"][0]["attributes"]["fileName"]
    img = fetch(f"https://uploads.mangadex.org/covers/{uuid}/{fn}.256.jpg")
    return img if len(img) > 5000 else None

def openlibrary(isbn):
    data = fetch(f"https://covers.openlibrary.org/b/isbn/{isbn}-M.jpg")
    return data if len(data) > 1000 else None
```

## git commit & pushフォーマット

commit後、毎回 `git push origin main` でVercelデプロイを起動する。

```
add: batch XX — 15 reviews (Title1, Title2, Title3, etc.)

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

## 3バッチ完了後の最終作業

3バッチのcommit & pushが完了したら、スプレッドシートを更新する：

```bash
python3 scripts/sync_sheets.py
```

## コンパクション後の再開方法

コンパクション発生時、次のターンでこのスキルを再度呼び出す必要はない。
サマリーに「何バッチ目まで完了済み」が記録されるので、そこから継続する。
