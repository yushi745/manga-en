# manga-en プロジェクト概要

日本の漫画を英語圏ユーザーに紹介するアフィリエイトサイト。
Amazon.com（Kindle / ペーパーバック / Omnibus）へのアフィリリンクで収益化。

---

## サイトコンセプト

- **ターゲット**: 日本漫画に興味のある英語圏ユーザー（北米・欧州）
- **コンテンツ**: 日本漫画のあらすじ・レビュー・おすすめ記事（英語）
- **収益**: Amazon Associates US（直接登録）経由のアフィリリンク
- **対象作品**: 公式英語版が存在する作品（englishStatus が Complete または Ongoing）

---

## 執筆者ペルソナ「Yu」

全記事を「Yu」という架空の執筆者が書いている体裁にする。

- **名前**: Yu
- **国籍**: 日本人・日本在住
- **バックストーリー**: 小学生のころいじめで孤立、友達ゼロ。漫画が唯一の逃げ場だった。ナルト・ワンピースのヒーローに憧れて育った。大人になって「日本の漫画の良さを世界に伝えたい」と思いこのサイトを始めた。
- **スタンス**: 英語は得意じゃない。でも漫画への愛は本物。完璧な英語じゃなくても、一生懸命届ける。
- **文体**: 丁寧だが熱量がある。一人称は "I"。読者への語りかけは "you"。
- **レビュー切り口**: 「この漫画が自分の人生にどう刺さったか」「どのシーンが忘れられないか」

---

## 記事フォーマット（frontmatter）

```markdown
---
title: "Naruto Review: The Story That Taught Me What It Means to Never Give Up"
slug: "naruto"
genre: "Action / Adventure"
genreSlug: "action"
mangaTitle: "Naruto"
mangaAuthor: "Masashi Kishimoto"
serialization: "Weekly Shonen Jump"
publisher: "Shueisha / VIZ Media"
volumes: 72
status: "Completed"              # Completed / Ongoing / Hiatus
englishVolumes: 72               # 英語版の刊行済み巻数
englishStatus: "Complete"        # Complete / Ongoing / Unlicensed
ageRating: "T (Teen)"            # All Ages / T (Teen) / M (Mature) / 18+
contentWarnings: ["violence", "mild language"]
description: "A comprehensive review of Naruto..."
coverImage: "https://..."
amazonASIN: "B00FPLNYUU"
publishedAt: "2026-04-23"
tags: ["shonen", "ninja", "action", "classic"]
rating: 5
hasAffiliate: true               # FTC開示フラグ（アフィリリンクあり記事はtrue）
---
```

---

## 記事テンプレート（全18セクション）

```
1.  frontmatter
2.  ## Quick Take（3行ポイント・箇条書き）
3.  ## Who Is This Manga For?（おすすめ読者・4項目）
4.  ## Content Warnings & Age Rating
5.  ## Yu's Rating（5軸テーブル）
6.  ## Story Overview（あらすじ）
7.  ## Characters（主要キャラ紹介）
8.  ## Art Style（絵柄・画風）
9.  ## Cultural Context（日本文化の背景）
10. ## What I Love About It（Yuの個人的な熱量・体験）
11. ## What English-Speaking Fans Say（Reddit/Goodreadsの傾向を自分の言葉で）
12. ## Memorable Scene ⚠️ Spoiler Warning（印象的なシーン）
13. ## Similar Manga（"If you liked X, try this"）
14. ## Reading Order / Where to Start（どの巻から買うべきか）
15. ## Official English Translation Status（英語版の状況）
16. ## Pros & Cons（購買判断の最終チェック）
17. ## Format Comparison（Physical / Digital / Omnibus の比較）
18. ## Where to Buy（AmazonリンクCTA）
    FTC Disclosure（フッター固定）
```

### Yu's Rating 5軸

| 項目 | スコア |
|------|--------|
| Story Depth | ★★★★★ |
| Art Style | ★★★★☆ |
| Character Development | ★★★★★ |
| Accessibility for Non-Japanese Readers | ★★★☆☆ |
| Reread Value | ★★★★☆ |

### Content Warnings の記載例

```markdown
## Content Warnings & Age Rating

**Age Rating**: T (Teen)
**Content Warnings**: Mild violence, themes of loss

Safe for most readers. Nothing graphic.
```

### FTC Disclosure（フッター固定文言）

```
This post contains affiliate links. If you purchase through these links,
I may earn a small commission at no extra cost to you. As an Amazon Associate,
I earn from qualifying purchases.
```

---

## スラッグ命名ルール（厳守）

- `-manga` サフィックスは**付けない**（`basara`、`mashle`、`bleach`）
- ローマ字は**ヘボン式**で統一（`busou-renkin`、`fullmetal-alchemist`）
- 英題がある場合は英題ベース（`blade-of-the-immortal`、`classroom-of-the-elite`）
- 冠詞 `the-` は**含める**（`blade-of-the-immortal` ○、`blade-of-immortal` ✗）
- スピンオフ・外伝は本編スラッグ + `-spinoff` 等で区別する

---

## 重複チェック（バッチ実行前に必須）

**記事を作る前に必ず以下で既存の `mangaTitleJa` と `mangaTitle` を照合する：**

```python
import re, glob

def load_existing(articles_dir="src/content/articles"):
    titles_ja, titles_en, slugs = set(), set(), set()
    for f in glob.glob(f"{articles_dir}/**/*.md", recursive=True):
        slugs.add(f.split("/")[-1].replace(".md", ""))
        for line in open(f, encoding="utf-8"):
            if line.startswith("mangaTitleJa:"):
                t = re.sub(r'^mangaTitleJa:\s*"?|"?\s*$', "", line).strip()
                titles_ja.add(t)
            elif line.startswith("mangaTitle:"):
                t = re.sub(r'^mangaTitle:\s*"?|"?\s*$', "", line).strip().lower()
                titles_en.add(t)
    return titles_ja, titles_en, slugs

# 使い方：バッチ対象リストを絞り込む前に実行
titles_ja, titles_en, slugs = load_existing()
# planned_ja = "鬼滅の刃" などと比較して既存なら SKIP
```

照合ルール：
- `mangaTitleJa` が一致 → 確実に重複、スキップ
- `mangaTitle`（小文字）が一致 → 重複、スキップ
- スラッグが一致 → ファイル上書きになるため必ずスキップ

---

## 記事生成ワークフロー

1. **重複チェック**（上記スクリプトで既存タイトルと照合してから作業開始）
2. **WebFetch** で日本語ネタバレ・あらすじサイトを参照して情報収集
3. 収集した情報をYuのペルソナで書き直す（コピーペーストではなく自分の言葉で）
4. `mangaTitleJa`（日本語タイトル）を frontmatter に追加する（Jikan APIで取得）
5. `src/content/articles/<genre>/<slug>.md` に保存（`coverImage` フィールドは**書かない**）
6. **カバー画像取得**（下記フロー参照）— MDファイル保存後に別途実行
7. git commit & push → Vercel自動デプロイ
8. **スプレッドシート更新**（3バッチ完了ごとに実行）
   ```bash
   python3 scripts/sync_sheets.py
   ```
   - `/batch-manga` スキルの3バッチ完了後に毎回実行する。

### バッチスクリプトの絶対ルール

- **`coverImage` フィールドをMDに書いてはならない**（OpenLibraryは画像が不正確なため全面禁止）
- カバー画像は必ず `python3 scripts/download_covers_rakuten.py` で別途取得する
- OpenLibrary・MangaDex・ハードコードISBNによる画像取得は禁止

---

## カバー画像取得フロー（確定）

バッチ記事作成後、`scripts/download_covers_rakuten.py` を実行して一括取得。
失敗した記事のみ以下の順で個別対応する。

### ステップ1: 楽天Books API（主）
- `mangaTitleJa`（日本語タイトル）で検索
- `scripts/download_covers_rakuten.py` が自動実行
- エンドポイント: `https://openapi.rakuten.co.jp/services/api/BooksBook/Search/20170404`
- キー: `.env.local` の `RAKUTEN_APP_ID` / `RAKUTEN_ACCESS_KEY`
- `Origin: https://www.dearmanga.com` ヘッダー必須

### ステップ2: Google Books API（補助）
- 楽天でNOT FOUNDの場合、同スクリプトが自動でフォールバック
- 追加の設定不要

### ステップ3: 個別対応（失敗した記事のみ）
1. `amazon.co.jp` で正式な日本語タイトルを確認
2. `mangaTitleJa` を修正
3. 楽天APIで再検索（スクリプト or 手動）

### ステップ4: 目視確認（必須）
`download_covers_rakuten.py` 実行後、バッチ全記事のカバー画像を Read ツールで1枚ずつ開いて目視確認する。
- タイトル文字・キャラ・デザインが `mangaTitle` と一致すること
- 別作品・Coming Soon・真っ白・ロゴのみ → NGとして coverImage 削除 + 画像ファイル削除
- **目視確認なしでコミット禁止**

### ステップ5: coverImage 削除
- ステップ3でも見つからない場合、またはステップ4でNGの場合は `coverImage` フィールドを frontmatter から削除
- 画像なし表示になる（page.tsx が `coverImage` の有無で条件分岐済み）

### 注意
- MangaDexは使わない（非公式・著作権グレー・URL不安定）
- ASINを推測・でっち上げしてはならない（Amazonリンクは現在すべて検索URLで運用中）

### ISBN取得スクリプト例（バッチ処理時）

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

※ よみほと違い `quality: "auto"` フラグ・noindexロジックは不要。最初から完成記事として作成する。

---

## アフィリエイト設計

- Associates ID: （登録後に記入）
- リンク形式: `https://www.amazon.com/dp/<ASIN>?tag=<associate-id>`
- 報酬受取: Payoneer（USD）
- Creators API: 直近30日10件以上の販売後に申請（それまでは手動リンク）
- FTC開示: 全アフィリリンク記事に `hasAffiliate: true` をセットし、フッターに固定表示

---

## ジャンル一覧

- `action` — アクション・少年漫画
- `romance` — 恋愛・少女漫画
- `fantasy` — ファンタジー・異世界
- `horror` — ホラー・サスペンス
- `slice-of-life` — 日常系
- `sports` — スポーツ
- `sci-fi` — SF・サイバーパンク

---

## 技術スタック

よみほ（`~/Documents/amazon-seo`）と同じ構成:
- Next.js (App Router) + TypeScript + Tailwind CSS
- Markdownファイルで記事管理（gray-matter / next-mdx-remote）
- GitHub → Vercel で自動デプロイ

詳細な構築手順: `SETUP.md`（このフォルダ内）
よみほの実装参照: `~/Documents/amazon-seo/src/`
