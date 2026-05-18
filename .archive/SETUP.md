# サイト構築基準書 — Next.js + GitHub + Vercel

よみほ（yomiho.jp）と同じ技術スタックでサイトを作るための手順書。
このドキュメント通りに進めれば同じ仕組みのサイトが作れる。

---

## 全体の流れ

```
1. ローカルでNext.jsプロジェクト作成
2. GitHubリポジトリ作成 → push
3. Vercelでデプロイ（GitHub連携）
4. 独自ドメイン設定（任意）
5. 記事MDファイルを追加 → push → 自動デプロイ
```

---

## Step 1: 前提ツールの確認

ターミナルで以下を確認する。

```bash
node -v      # v18以上推奨
npm -v
git -v
```

GitHubアカウントとVercelアカウント（無料）が必要。

---

## Step 2: Next.jsプロジェクト作成

```bash
cd ~/Documents
npx create-next-app@latest <プロジェクト名> \
  --typescript \
  --tailwind \
  --eslint \
  --app \
  --no-src-dir=false \
  --import-alias "@/*"
```

対話形式で聞かれる場合の推奨回答：
- TypeScript: Yes
- ESLint: Yes
- Tailwind CSS: Yes
- `src/` directory: Yes
- App Router: Yes
- import alias: `@/*`（デフォルト）

---

## Step 3: 追加パッケージのインストール

よみほと同じ構成で記事をMarkdownで管理するためのパッケージ。

```bash
npm install gray-matter next-mdx-remote remark remark-gfm remark-html
npm install @tailwindcss/typography
```

| パッケージ | 役割 |
|-----------|------|
| `gray-matter` | Markdownファイルのfrontmatter（---〜---）を解析 |
| `next-mdx-remote` | MarkdownをReactコンポーネントとしてレンダリング |
| `remark` / `remark-gfm` | Markdownの変換処理 |
| `@tailwindcss/typography` | Markdownの文章を美しく表示するTailwindプラグイン |

---

## Step 4: フォルダ構成

```
src/
├── app/
│   ├── layout.tsx          # 全ページ共通レイアウト（header/footer）
│   ├── page.tsx            # トップページ
│   ├── globals.css         # グローバルCSS
│   ├── robots.ts           # robots.txt自動生成
│   ├── sitemap.ts          # sitemap.xml自動生成
│   └── [genre]/
│       ├── page.tsx        # ジャンル一覧ページ
│       └── [slug]/
│           └── page.tsx    # 個別記事ページ
├── components/
│   ├── Header.tsx
│   ├── Footer.tsx
│   ├── ArticleCard.tsx     # 記事一覧のカード
│   └── MarkdownContent.tsx # Markdownレンダリング
├── content/
│   └── articles/
│       ├── action/         # ジャンル別フォルダ
│       │   └── naruto.md
│       └── romance/
│           └── fruits-basket.md
└── lib/
    ├── types.ts            # 型定義
    └── articles.ts         # 記事の読み込みロジック
```

---

## Step 5: 記事ファイルの形式（Markdownフロントマター）

各記事は `src/content/articles/<genre>/<slug>.md` に作成する。

```markdown
---
title: "Naruto Review: The Greatest Ninja Story Ever Told"
slug: "naruto"
genre: "Action"
genreSlug: "action"
mangaTitle: "Naruto"
mangaAuthor: "Masashi Kishimoto"
publisher: "Shueisha"
volumes: 72
description: "A comprehensive review of Naruto..."
coverImage: "https://..."
amazonASIN: "B00FPLNYUU"
publishedAt: "2026-04-23"
tags: ["shonen", "ninja", "action"]
rating: 5
hasEnglish: true
---

## Summary
...
```

---

## Step 6: 記事読み込みロジック（lib/articles.ts の骨格）

```typescript
import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const articlesDir = path.join(process.cwd(), 'src/content/articles');

export function getAllArticles() {
  const genres = fs.readdirSync(articlesDir);
  const articles = [];

  for (const genre of genres) {
    const genreDir = path.join(articlesDir, genre);
    const files = fs.readdirSync(genreDir);

    for (const file of files) {
      const filePath = path.join(genreDir, file);
      const raw = fs.readFileSync(filePath, 'utf-8');
      const { data, content } = matter(raw);
      articles.push({ frontmatter: data, content, slug: data.slug, genreSlug: genre });
    }
  }

  return articles;
}

export function getArticleBySlug(genreSlug: string, slug: string) {
  const filePath = path.join(articlesDir, genreSlug, `${slug}.md`);
  const raw = fs.readFileSync(filePath, 'utf-8');
  const { data, content } = matter(raw);
  return { frontmatter: data, content };
}
```

---

## Step 7: GitHubリポジトリ作成 & push

```bash
cd ~/Documents/<プロジェクト名>

# Gitの初期化（create-next-appが自動でやっている場合はスキップ）
git init
git add .
git commit -m "initial commit"

# GitHubでリポジトリを作成してからpush
git remote add origin https://github.com/<username>/<repo-name>.git
git branch -M main
git push -u origin main
```

GitHubでのリポジトリ作成は github.com → New repository から。
Private でも Vercel は読める。

---

## Step 8: Vercelでデプロイ

1. [vercel.com](https://vercel.com) にログイン（GitHubアカウントで可）
2. 「Add New → Project」をクリック
3. GitHubリポジトリを選んで「Import」
4. 設定はほぼデフォルトのまま「Deploy」
5. 数分でデプロイ完了 → `https://<project-name>.vercel.app` で公開

**以降は `git push` するたびに自動でデプロイされる。**

---

## Step 9: 独自ドメイン設定（任意）

1. お名前.com や Cloudflare でドメイン取得
2. Vercel の Project Settings → Domains → 「Add Domain」
3. 表示されるDNSレコード（CNAMEまたはAレコード）をドメイン管理画面に設定
4. 数分〜数時間で反映

---

## Step 10: 記事追加の日常ワークフロー

```bash
# 1. 記事ファイルを src/content/articles/<genre>/<slug>.md に作成
# 2. ローカル確認
npm run dev        # http://localhost:3000 で確認

# 3. push → Vercelが自動デプロイ
git add src/content/articles/<genre>/<slug>.md
git commit -m "add: <manga title> review"
git push
```

---

## アフィリエイト設計（Amazon Associates US）

- Associates登録: https://affiliate-program.amazon.com
- アフィリリンクの形式: `https://www.amazon.com/dp/<ASIN>?tag=<associate-id>`
- 初期はリンクを手書きで埋め込む（Creators APIは月30件以上の販売後に申請）
- 報酬受取: Payoneer（USD対応）推奨

---

## よみほとの主な違い（このサイト固有の考慮点）

| 項目 | よみほ（日本語書籍） | このサイト（英語・漫画） |
|------|------|------|
| 言語 | 日本語 | 英語 |
| コンテンツ | 書籍レビュー | 漫画紹介・レビュー |
| アフィリ | もしもAmazon JP | Amazon Associates US直接 |
| 対象読者 | 日本語読者 | 英語圏の日本漫画ファン |
| 記事の軸 | 著者・ジャンル | タイトル・シリーズ・ジャンル |
| 特記事項 | KU対応フラグ | 英語版発売済みかフラグ（hasEnglish） |

---

## よみほの実際のソースコードを参照する場合

`~/Documents/amazon-seo/` がよみほのプロジェクトフォルダ。
- `src/lib/articles.ts` — 記事読み込みロジックの実装例
- `src/app/[genre]/[slug]/page.tsx` — 個別記事ページの実装例
- `src/components/` — 各コンポーネントの実装例
- `src/lib/types.ts` — フロントマターの型定義例
