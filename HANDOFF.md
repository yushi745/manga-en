# MangaWithYu 引き継ぎ資料

このファイルを読めば今の状態と次にやることが全部わかる。

---

## 現在の状態

| 項目 | 状態 |
|------|------|
| ローカル | `/Users/yushi/Documents/manga-en/` |
| GitHub | https://github.com/yushi745/manga-en |
| Vercel（本番） | https://manga-en.vercel.app |
| 独自ドメイン | 未取得 |
| Amazon Associates US | 未登録 |
| 記事数 | 0（サイトの骨格のみ） |

---

## 確定済みの決定事項

### サイト設計
- **サイト名**: MangaWithYu（仮。変更するなら `src/lib/types.ts` の `SITE_CONFIG` と Vercel のドメイン設定を変える）
- **対象**: 公式英語版が存在する日本漫画のみ
- **収益**: Amazon Associates US（直接登録）+ Payoneer（USD受取）
- **Creators API**: 月30件以上の販売後に申請予定。それまでは手動アフィリリンク

### ペルソナ「Yu」
- 日本人・日本在住
- 小学生のころいじめで孤立、漫画が唯一の逃げ場だった
- ナルト・ワンピースのヒーローに憧れて育った
- 英語は得意じゃないが漫画への愛は本物
- 「完璧な英語じゃなくても、一生懸命届ける」スタンス

### 記事テンプレート（18セクション・確定版）
```
1.  frontmatter
2.  ## Quick Take
3.  ## Who Is This Manga For?
4.  ## Content Warnings & Age Rating
5.  ## Yu's Rating（5軸: Story Depth / Art Style / Character Development / Accessibility / Reread Value）
6.  ## Story Overview
7.  ## Characters
8.  ## Art Style
9.  ## Cultural Context
10. ## What I Love About It
11. ## What English-Speaking Fans Say
12. ## Memorable Scene ⚠️ Spoiler Warning
13. ## Similar Manga
14. ## Reading Order / Where to Start
15. ## Official English Translation Status
16. ## Pros & Cons
17. ## Format Comparison（Physical / Digital / Omnibus）
18. ## Where to Buy（AmazonリンクCTA）
    FTC Disclosure（フッター固定）
```

### 記事生成ルール
- `quality: "auto"` フラグ不要（よみほと違い、最初から完成記事として作る）
- 記事生成時は **WebFetch** で日本語ネタバレ・あらすじサイトを参照して情報収集
- 収集情報はYuのペルソナで書き直す（コピペ禁止）
- frontmatterの `hasAffiliate: true` を付ければ記事内にFTC開示が自動表示される

### フロントマター形式
```yaml
---
title: "Naruto Review: ..."
slug: "naruto"
genre: "Action / Adventure"
genreSlug: "action"
mangaTitle: "Naruto"
mangaAuthor: "Masashi Kishimoto"
serialization: "Weekly Shonen Jump"
publisher: "Shueisha / VIZ Media"
volumes: 72
status: "Completed"           # Completed / Ongoing / Hiatus
englishVolumes: 72
englishStatus: "Complete"     # Complete / Ongoing / Unlicensed
ageRating: "T (Teen)"
contentWarnings: ["violence"]
description: "..."
coverImage: "https://..."
amazonASIN: "B00FPLNYUU"
publishedAt: "2026-04-23"
tags: ["shonen", "action"]
rating: 5
hasAffiliate: true
---
```

---

## 次にやること（優先順）

### 1. 独自ドメイン取得
- 候補: `mangawithyu.com`（サイト名と一致・シンプル）
- 取得先: Cloudflare（年約$10で安い）
- 取得後: Vercel の Project Settings → Domains → Add Domain

### 2. Amazon Associates US 登録
- URL: https://affiliate-program.amazon.com
- サイトURLとして `https://mangawithyu.com`（または現在のVercel URL）を登録
- 登録後: `.env.local` の `NEXT_PUBLIC_AMAZON_ASSOCIATE_TAG` にタグIDを設定
- Vercel にも環境変数を追加（Settings → Environment Variables）
- 180日以内に3件の販売が必要（未達でアカウントクローズ、再申請可）

### 3. 試しに1記事作成
- ナルトあたりから始めると情報が豊富で書きやすい
- `src/content/articles/action/naruto.md` に作成
- git push → Vercel自動デプロイで即公開確認

### 4. 記事を増やす
- 人気タイトルから順に（ナルト・ワンピース・鬼滅・進撃・ハイキュー etc.）
- 英語版が出ている作品のみ対象
- WebFetchで日本語ネタバレサイトを参照しながら作成

---

## 技術メモ

### 記事追加の手順
```bash
# 1. 記事ファイルを作成
# src/content/articles/<genre>/<slug>.md

# 2. ローカル確認
npm run dev   # http://localhost:3000

# 3. push → 自動デプロイ
git add src/content/articles/<genre>/<slug>.md
git commit -m "add: <manga title> review"
git push
```

### アフィリリンクの形式
```
https://www.amazon.com/dp/<ASIN>?tag=<associate-id>
```
Associate IDが未設定の間はタグなしのAmazon URLが出力される（動作はする）。

### 環境変数（.env.local）
```
NEXT_PUBLIC_AMAZON_ASSOCIATE_TAG=（登録後に設定）
```
Vercel にも同じ変数を追加することを忘れずに。

### ジャンルフォルダ
```
src/content/articles/
├── action/
├── romance/
├── fantasy/
├── horror/
├── slice-of-life/
├── sports/
└── sci-fi/
```

### よみほの実装を参考にする場合
`~/Documents/amazon-seo/src/` を参照。
