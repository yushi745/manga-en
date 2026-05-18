# 記事テンプレート詳細 / Article Templates

→ このファイルはCLAUDE.mdから参照される補助ファイル。記事執筆時に使う固定文言・フォーマットをまとめている。

---

## Where to Buy テンプレート（固定文言）

**英語版あり（englishStatus: Complete / Ongoing）**
```
## Where to Buy

Read the first volume. If it doesn't hook you, put it down. It'll hook you.

[Start with Volume 1 →](Amazon URL)
```

**Unlicensed（englishStatus: Unlicensed）**
```
## Where to Buy

No English release yet. That just means you find it before everyone else does.
```

---

## Yu's Rating 5軸テーブル

| 項目 | スコア |
|------|--------|
| Story Depth | ★★★★★ |
| Art Style | ★★★★☆ |
| Character Development | ★★★★★ |
| Accessibility for Non-Japanese Readers | ★★★☆☆ |
| Reread Value | ★★★★☆ |

---

## Content Warnings の記載例

```markdown
## Content Warnings & Age Rating

**Age Rating**: T (Teen)
**Content Warnings**: Mild violence, themes of loss

Safe for most readers. Nothing graphic.
```

---

## Similar Manga フォーマット（3列テーブル）

```markdown
## Similar Manga

| Title | Its Approach | How [This Manga] Differs |
|---|---|---|
| Manga A | What it does | What this does differently |
| Manga B | What it does | What this does differently |
```

- 箇条書きではなく3列テーブルを使う
- 列3は "How [This Manga] Differs" の [This Manga] を実際のタイトルに変える

---

## FTC Disclosure（フッター固定文言）

```
This post contains affiliate links. If you purchase through these links,
I may earn a small commission at no extra cost to you. As an Amazon Associate,
I earn from qualifying purchases.
```

---

## ISBN取得スクリプト例

```python
import urllib.request, urllib.parse, json

def get_isbn(title, author=""):
    query = urllib.parse.quote(f"{title} {author}".strip())
    url = f"https://openlibrary.org/search.json?q={query}&limit=5"
    with urllib.request.urlopen(url, timeout=10) as r:
        data = json.loads(r.read())
    for doc in data.get('docs', []):
        isbns = doc.get('isbn', [])
        isbn10 = [i for i in isbns if len(i) == 10]
        if isbn10:
            return isbn10[0]
    return None
```
