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

## 記事生成ワークフロー

1. **WebFetch** で日本語ネタバレ・あらすじサイトを参照して情報収集
2. 収集した情報をYuのペルソナで書き直す（コピーペーストではなく自分の言葉で）
3. `src/content/articles/<genre>/<slug>.md` に保存
4. git commit & push → Vercel自動デプロイ

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
