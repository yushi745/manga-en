# manga-en プロジェクト概要

日本の漫画を英語圏ユーザーに紹介するアフィリエイトサイト。
Amazon.com（Kindle / ペーパーバック / Omnibus）へのアフィリリンクで収益化。

**本番サイト**: https://www.dearmanga.com/
**技術スタック**: Next.js (App Router) + TypeScript + Tailwind CSS / GitHub → Vercel 自動デプロイ

---

## サブファイル一覧

| ファイル | 内容 |
|---|---|
| `CLAUDE-article.md` | 単一タイトル記事のセクション構成・品質ルール・自己チェックリスト |
| `CLAUDE-guide.md` | まとめ記事・ガイド記事のルール（今後作成） |
| `CLAUDE-templates.md` | Where to Buy・FTC・固定文言・テーブルフォーマット |
| `CLAUDE-covers.md` | カバー画像取得フロー・Pythonスクリプト |

---

## サイトコンセプト

- **ターゲット**: 日本漫画に興味のある英語圏ユーザー（北米・欧州）
- **コンテンツ**: 日本漫画のレビュー・おすすめまとめ記事（英語）
- **収益**: Amazon Associates US（tag=dearmanga-20はプレースホルダー）/ JP tag: yushi745-22登録済み
- **対象作品**: 公式英語版が存在する作品（englishStatus が Complete または Ongoing）

---

## 執筆者ペルソナ「Yu」

全記事を「Yu」という架空の執筆者が書いている体裁にする。

- **名前**: Yu / 日本人・日本在住
- **バックストーリー**: 小学生のころいじめで孤立、友達ゼロ。漫画が唯一の逃げ場だった。ナルト・ワンピースのヒーローに憧れて育った。大人になって「日本の漫画の良さを世界に伝えたい」と思いこのサイトを始めた。
- **スタンス**: 英語は得意じゃない。でも漫画への愛は本物。完璧な英語じゃなくても、一生懸命届ける。
- **文体**: 丁寧だが熱量がある。一人称は "I"。読者への語りかけは "you"。
- **レビュー切り口**: 「この漫画が自分の人生にどう刺さったか」「どのシーンが忘れられないか」

---

## frontmatterフォーマット（全記事共通）

```markdown
---
title: "..."
slug: "naruto"
genre: "Action / Adventure"
genreSlug: "action"
mangaTitle: "Naruto"
mangaTitleJa: "ナルト"
mangaAuthor: "Masashi Kishimoto"
serialization: "Weekly Shonen Jump"
publisher: "Shueisha / VIZ Media"
volumes: 72
status: "Completed"              # Completed / Ongoing / Hiatus
englishVolumes: 72
englishStatus: "Complete"        # Complete / Ongoing / Unlicensed
ageRating: "T (Teen)"            # All Ages / T (Teen) / M (Mature) / 18+
contentWarnings: ["violence", "mild language"]
description: "..."
amazonASIN: "B00FPLNYUU"
publishedAt: "2026-04-23"        # 過去日付・バラけさせる。未来日付禁止
tags: ["shonen", "ninja", "action"]
rating: 5
hasAffiliate: true
---
```

※ `coverImage` はMD作成時点で書かない。画像取得後に追加（`CLAUDE-covers.md` 参照）。

---

## スラッグ命名ルール（厳守）

- `-manga` サフィックスは付けない（`basara`、`mashle`、`bleach`）
- ローマ字はヘボン式で統一（`busou-renkin`、`fullmetal-alchemist`）
- 英題がある場合は英題ベース（`blade-of-the-immortal`、`classroom-of-the-elite`）
- 冠詞 `the-` は含める（`blade-of-the-immortal` ○、`blade-of-immortal` ✗）
- スピンオフ・外伝は本編スラッグ + `-spinoff` 等で区別する

---

## 重複チェック（バッチ実行前に必須）

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

titles_ja, titles_en, slugs = load_existing()
```

照合ルール: `mangaTitleJa` 一致 / `mangaTitle`（小文字）一致 / スラッグ一致 → いずれもスキップ

**実行タイミング**: バッチ開始前 + 各バッチのgit commit直後（次のバッチ前）に必ず実行。

---

## 記事生成ワークフロー

1. **重複チェック**（上記スクリプトで照合）
2. **事前調査 + 執筆**（`CLAUDE-article.md` の手順に従う）
3. `src/content/articles/<genre>/<slug>.md` に保存
4. **自己チェック**（`CLAUDE-article.md` のチェックリストを実行）
5. **カバー画像取得**（`CLAUDE-covers.md` の手順に従う）
6. git commit & push → Vercel自動デプロイ
7. **スプレッドシート更新**
   ```bash
   python3 scripts/sync_sheets.py
   ```
   **実行タイミング（記事に変更を加えた場合は必ず実行）：**
   - 新規記事を作成したとき
   - 記事をリライトしたとき（`rewritten:` フィールド追加時）
   - カバー画像を追加・削除・差し替えしたとき
   - `noindex` フラグを変更したとき
   - frontmatterを変更したとき（slug・genre・status・タイトル等）
   - ファイルを移動・リネームしたとき

---

## ジャンル一覧

- `action` — アクション・少年漫画
- `romance` — 恋愛・少女漫画
- `fantasy` — ファンタジー・異世界
- `horror` — ホラー・サスペンス
- `slice-of-life` — 日常系
- `sports` — スポーツ
- `sci-fi` — SF・サイバーパンク
