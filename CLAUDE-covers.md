# カバー画像取得フロー

→ このファイルはCLAUDE.mdから参照される補助ファイル。バッチ記事作成後のカバー画像取得手順をまとめている。

---

## 禁止事項（絶対厳守）

- `coverImage` フィールドをMD作成時点で書いてはならない（画像取得後に追加する）
- `scripts/download_covers_rakuten.py` は使用禁止（全記事を上書きするため）
- OpenLibrary・MangaDex・ハードコードISBNによる画像取得は禁止
- ASINを推測・でっち上げしてはならない

---

## ステップ1: 楽天Books API（主）+ Google Books（補助）

バッチ対象スラッグのみを対象にしたインラインPythonで実行する。

```python
import urllib.request, urllib.parse, json, os, time, re

RAKUTEN_APP_ID = open("/Users/yushi/Documents/manga-en/.env.local").read()
RAKUTEN_APP_ID = re.search(r"RAKUTEN_APP_ID=(\S+)", RAKUTEN_APP_ID).group(1)

SLUGS = ["slug-1", "slug-2", ...]  # バッチ対象スラッグのみ

def get_title_ja(slug):
    import glob
    for f in glob.glob(f"src/content/articles/**/{slug}.md", recursive=True):
        for line in open(f):
            if line.startswith("mangaTitleJa:"):
                return re.sub(r'^mangaTitleJa:\s*"?|"?\s*$', "", line).strip()
    return None

def rakuten(title):
    q = urllib.parse.quote(title)
    url = f"https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?applicationId={RAKUTEN_APP_ID}&title={q}&hits=3&imageFlag=1"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "manga-en/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            j = json.loads(r.read())
        items = j.get("Items", [])
        if items:
            img_url = items[0]["Item"]["largeImageUrl"]
            with urllib.request.urlopen(img_url, timeout=10) as r:
                data = r.read()
            return data if len(data) > 5000 else None
    except: pass
    return None

def google_books(title):
    q = urllib.parse.quote(title)
    try:
        with urllib.request.urlopen(f"https://www.googleapis.com/books/v1/volumes?q={q}&maxResults=5", timeout=10) as r:
            j = json.loads(r.read())
        for item in j.get("items", []):
            img = item.get("volumeInfo", {}).get("imageLinks", {}).get("thumbnail", "")
            if img:
                img = img.replace("zoom=1", "zoom=3").replace("http://", "https://")
                with urllib.request.urlopen(img, timeout=10) as r:
                    data = r.read()
                if len(data) > 5000:
                    return data
    except: pass
    return None

for slug in SLUGS:
    out = f"public/covers/{slug}.jpg"
    if os.path.exists(out): print(f"SKIP {slug}"); continue
    title = get_title_ja(slug)
    if not title: print(f"NO TITLE {slug}"); continue
    data = rakuten(title) or google_books(title)
    if data:
        open(out, "wb").write(data)
        print(f"OK {slug} ({len(data)})")
    else:
        print(f"FAIL {slug}")
    time.sleep(0.3)
```

---

## ステップ2: coverImage フィールドをMDに追加

```bash
for slug in slug-1 slug-2 ...; do
  f=$(find src/content/articles -name "${slug}.md")
  if [ -f "public/covers/${slug}.jpg" ]; then
    sed -i '' "s|^slug: \"${slug}\"|slug: \"${slug}\"\ncoverImage: \"/covers/${slug}.jpg\"|" "$f"
  fi
done
```

---

## ステップ3: 目視確認（必須・コミット前）

バッチ全記事のカバー画像をReadツールで1枚ずつ開いて確認する。

- タイトル文字・キャラ・デザインが `mangaTitle` と一致すること
- 別作品・Coming Soon・真っ白・ロゴのみ → NG

---

## ステップ4: NG画像の処理

- `coverImage` フィールドをfrontmatterから削除
- `public/covers/<slug>.jpg` を削除
- 画像なし表示になる（page.tsxが `coverImage` の有無で条件分岐済み）

---

## APIで取得できなかった場合: ChromeMCPで手動取得

楽天API・Google Books APIで両方FAILした場合は**ChromeMCPで手動取得する**（恒久ルール）。

1. ChromeMCPで `books.rakuten.co.jp` を開く
2. 日本語タイトルで検索
3. 正しい本が検索結果に出たことを**目視確認**
4. 画像URLを取得して `public/covers/<slug>.jpg` に保存
5. frontmatterに `coverImage: "/covers/<slug>.jpg"` を追加
6. コミット&プッシュ

**注意:** ChromeMCPは1つのChrome接続に1クライアントのみ。他のセッションで使用中の場合は待つ。
