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

## 記事テンプレート（全19セクション）

```
1.  frontmatter
    ※ title のサブタイトル部分は「一言キャッチ」にする
      良い例: "A Basketball Manga Where Effort Doesn't Beat Reality"
      悪い例: "The Basketball Manga That Never Gives Up" （説明的すぎる）
      ルール: 作品の「逆説・核心・意外性」を1フレーズで。読んだ人が誰かに話したくなる言葉を選ぶ。

2.  冒頭フック（1〜2文、セクション見出しなし）
    ※ frontmatter 直後、## Quick Take の前に置く
    ※ 「問い」か「違和感」か「逆説」で始める。読者を1秒で引き込む一文。
      良い例:
        "What if the most dangerous place in Japan isn't a battlefield — it's a high school nobody chose to attend?"
        "What if effort is never enough? Not as a lesson. As a rule."
        "This is not a romance manga. It just happens to end that way."
      悪い例: "This is a great manga about basketball." （情報で始めない）

3.  ## Quick Take（3行ポイント・箇条書き）
4.  ## Who Is This Manga For?（おすすめ読者・4項目）
5.  ## Content Warnings & Age Rating
6.  ## Yu's Rating（5軸テーブル）
7.  ## Story Overview（あらすじ）
8.  ## Characters（主要キャラ紹介）
9.  ## Art Style（絵柄・画風）
10. ## Cultural Context（日本文化の背景）
11. ## What I Love About It（Yuの個人的な熱量・体験）
12. ## What English-Speaking Fans Say（Reddit/Goodreadsの傾向を自分の言葉で）
13. ## Memorable Scene ⚠️ Spoiler Warning（印象的なシーン）
14. ## Similar Manga（"If you liked X, try this"）
15. ## Reading Order / Where to Start（どの巻から買うべきか）
16. ## Official English Translation Status（英語版の状況）
17. ## Pros & Cons（購買判断の最終チェック）
    ※ Consの最後に「this won't work for everyone」系フレーズを1行加える
      例: "The pacing is slow — that's either a flaw or a feature depending on you."
      例: "The style is an acquired taste. It won't land for everyone."
      例: "If you need fast pacing, this isn't your book."
      理由: 読者に「自分向きか判断する余地」を与えることでクリック率が上がる

18. ## Is [Manga Title] Worth Reading?（SEO H2・新規追加）
    ※ 検索クエリ "Is [X] worth reading?" を拾うためのセクション
    ※ Pros & Consを1〜2文で凝縮してまとめ直すだけでOK（重複コンテンツでよい）
    ※ タイトルは作品名を入れて "Is [Manga Title] Worth Reading?" を基本形にする
      例: "Is Do Not Say Mystery Worth Reading?"
      例: "Is Vinland Saga Worth Reading?"

19. ## Format Comparison（Physical / Digital / Omnibus の比較）
20. ## Where to Buy（AmazonリンクCTA）
    FTC Disclosure（フッター固定）
```

### Where to Buy テンプレート（固定文言）

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

### Similar Manga フォーマット（3列テーブル）

```markdown
## Similar Manga

| Title | Its Approach | How [This Manga] Differs |
|---|---|---|
| Manga A | What it does | What this does differently |
| Manga B | What it does | What this does differently |
```

※ 箇条書きではなく3列テーブルを使う
※ 「違い」を明示することで「この作品を選ぶ理由」が一目で伝わる
※ 列3は "How [This Manga] Differs" の [This Manga] を実際のタイトルに変える

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

**重複チェックのタイミング（必須）：**
- バッチ開始前（セッション開始時）に1回
- **各バッチのgit commit直後、次のバッチ開始前にも必ず再実行**
- 同一セッション内の複数バッチでも毎回実行すること（バッチ1の記事がバッチ2の候補に重複する可能性があるため）

---

## 記事品質ルール（リライト・新規共通）

goodnight-punpunのリライト（2026-05-17）を基準にした品質基準。新規記事・リライトともに適用する。

### 事前調査（必須）

1. **Search Consoleのクエリデータを確認する**
   - そのスラッグに来ている検索クエリを確認し、ユーザーが何を知りたいかを特定する
   - 上位クエリが問いかけている内容は記事内でH2セクションとして答える
   - 例: "why is punpun drawn as a bird" が上位クエリ → "## Why Is Punpun Drawn as a Bird?" セクションを作る

2. **日本語ソースをWebFetchで読み込む**
   - Wikipedia日本語版・ニコニコ大百科・ファン考察サイトを複数参照する
   - 目的: 「その作品でしか書けない具体的な事実」を収集すること
   - 収集する情報: 具体的なシーン・台詞・キャラの行動・各章の転換点・結末の構造

### セクション別品質基準

**冒頭フック（## Quick Take の前）**
- Yuの個人的な記憶・体験から始める（「問い」だけで始めるのは禁止）
- 例: 中学時代の思い出 → この漫画との接続、という流れ
- 読者がYuという人間を感じられる1〜3段落

**## Story Overview**
- あらすじを「概要」で終わらせない
- 含めるべき内容: 序盤の核心的な出来事・物語の転換点・結末の構造（ネタバレ警告なしで書いてよい）
- 「ネタバレになるから書かない」は禁止 — 読者は買う前に内容を知りたい

**## Characters**
- 各キャラクターの「実際のアーク」を書く（性格説明だけでは不十分）
- 例: 「アイコは転校生でプンプンの初恋」ではなく、「アイコは鹿児島の約束を13年間抱えたまま、種子島で死ぬ」
- 主要キャラは最低3〜4人、各人100字以上

**## What I Love About It**
- 特定のシーン・コマ・台詞を1つ選んで深く掘り下げる（最重要セクション）
- 「このシーンが好き」ではなく「このシーンのどの要素が・なぜYuに刺さったか」
- 最低2段落。「感動した」「泣いた」で終わる文は書かない

**## Memorable Scene ⚠️ Spoiler Warning**
- 具体的なシーンを描写する。「〜のシーンが印象的」で終わらない
- 何が起きたか・ページがどう見えるか・なぜ頭から離れないかを書く
- 「意図的に曖昧にした」「解釈は読者に委ねる」系の逃げは禁止

**## Similar Manga**
- 必ず3列テーブル形式（箇条書き禁止）
- 列3は "How [This Manga] Differs" — 差異を明示する

**ageRating の扱い**
- Quick Takeの3番目の箇条書きに必ず明示する
- 例: `"Age rating: **M (Mature)** — violence, sexual content"`
- M/18+作品はContent Warnings冒頭にも太字で繰り返す

### テンプレートの使い方

- 全19セクションを機械的に埋めない。その作品で一番語れるセクションを2倍の長さにして、薄くなるセクションは削るか短くする
- 「Cultural Context」「Art Style」が薄くなる場合は2〜3文でまとめてよい。その分を「What I Love」「Memorable Scene」に回す
- テンプレートは骨格であって、分量の均等配分ではない

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
- カバー画像は**バッチ対象スラッグのみ**をターゲットにしたインラインPythonで個別取得する
- `scripts/download_covers_rakuten.py` は**絶対に使わない**（全記事を上書きするため）
- OpenLibrary・MangaDex・ハードコードISBNによる画像取得は禁止

### APIで取得できなかったカバー画像はChromeMCPで取得する（恒久ルール）

楽天API・Google Books APIで取得できなかった画像は、**ChromeMCPを使って手動取得する**。特定バッチに限らず、今後APIで失敗した全件に適用する。

手順：
1. ChromeMCPで `books.rakuten.co.jp` を開く
2. 日本語タイトルで検索
3. 正しい本が検索結果に出たことを**目視確認**
4. 画像URLを取得して `public/covers/<slug>.jpg` に保存
5. frontmatterに `coverImage: "/covers/<slug>.jpg"` を追加
6. コミット&プッシュ

**注意：** ChromeMCPは1つのChrome接続に1クライアントのみ接続可能。他のセッションで使用中の場合は待ってから実行する。

---

## カバー画像取得フロー（確定）

バッチ記事作成後、**バッチ対象スラッグだけ**を対象にしたインラインPythonスクリプトを書いて実行する。
`scripts/download_covers_rakuten.py` は全記事を上書きするため使用禁止。

### ステップ1: 楽天Books API（主）+ Google Books（補助）のインラインスクリプト

バッチ対象スラッグのリストを明示し、そのスラッグに対応する MD ファイルから `mangaTitleJa` を読み取って検索する。

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

### ステップ2: coverImage フィールドを MD に追加

```bash
for slug in slug-1 slug-2 ...; do
  f=$(find src/content/articles -name "${slug}.md")
  if [ -f "public/covers/${slug}.jpg" ]; then
    sed -i '' "s|^slug: \"${slug}\"|slug: \"${slug}\"\ncoverImage: \"/covers/${slug}.jpg\"|" "$f"
  fi
done
```

### ステップ3: 目視確認（必須）
バッチ全記事のカバー画像を Read ツールで1枚ずつ開いて目視確認する。
- タイトル文字・キャラ・デザインが `mangaTitle` と一致すること
- 別作品・Coming Soon・真っ白・ロゴのみ → NGとして coverImage 削除 + 画像ファイル削除
- **目視確認なしでコミット禁止**

### ステップ4: coverImage 削除
- ステップ3でNGの場合は `coverImage` フィールドを frontmatter から削除
- 画像なし表示になる（page.tsx が `coverImage` の有無で条件分岐済み）

### 注意
- `scripts/download_covers_rakuten.py` は**使用禁止**（全記事上書きするため）
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
