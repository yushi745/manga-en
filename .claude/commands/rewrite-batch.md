# /rewrite-batch

manga-enプロジェクトの既存記事を1バッチ（15記事）フルリライトしてコミットする。

---

## 実行前に必ず読むこと（毎回・例外なし）

バッチ開始前に以下のファイルを**必ずRead**する：

1. `CLAUDE-article.md` — リライト判定ルール・セクション構成・チェックリスト
2. `CLAUDE-templates.md` — Where to Buy・FTC・テーブルフォーマット

これを飛ばしてリライトを始めることは禁止。

---

## ジャンルローテーション優先順

以下の順で循環する。`git log` で前回バッチのジャンルを確認し、次のジャンルから取る。

```
action → romance → fantasy → horror → slice-of-life → sports → sci-fi → action → ...
```

対象ジャンル内で `read: true` のない記事をファイル名アルファベット順に15件選ぶ。

---

## 1記事あたりの手順（必ずこの順で）

1. **記事ファイルを Read**（現状把握）
2. **WebFetch / WebSearch で情報取得**（2ソース以上。Wikipedia・出版社ページ・ネタバレブログ等）
   - 取れた → フルリライトへ
   - 取れなかった → アーカイブ（`git mv` で `src/content/archived/<genre>/<slug>.md`）
3. **Write でファイルを丸ごと書き直す**（Editでの部分修正は禁止）
   - `read: true` を必ず付与
   - `rewritten: "YYYY-MM-DD"` を追加
   - `coverImage` は既存値があればそのまま維持。なければ書かない
   - `publishedAt` は過去日付のまま維持（変更しない）
4. **レビューエージェントで独立検証**（`Agent` tool、`subagent_type: "general-purpose"`）
   - frontmatter事実・What I Love・Memorable Sceneのシーン・Story Overviewを裏取り
   - OK → コミット対象に追加
   - FLAGGED → 修正 → 再検証 → それでも無理なら archive
5. 次の記事へ

---

## バッチ完了後

15記事（アーカイブ含む）が終わったら：

1. `git add` + `git commit`
   ```
   rewrite: batch N — 15 <genre> articles (verified-by-reviewer)

   Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
   ```
2. `git push origin main`
3. `python3 scripts/sync_sheets.py`

---

## ユーザーへの完了報告フォーマット

```
## 完了記事（バッチN）

### <記事タイトル>
- URL: https://www.dearmanga.com/<genreSlug>/<slug>
- 検証済み内容: <具体的な裏取り内容>
- レビュー結果: OK / FLAGGED→修正済

---

（アーカイブした場合）
### アーカイブ: <slug>
- 理由: <なぜWebFetchでデータが取れなかったか>
```

---

## 禁止事項（要約）

- frontmatterだけ修正して `read: true` を付ける
- `Edit` で部分修正してリライト完了とする
- ソースなしで想像書き・キャラ心情の補完
- `publishedAt` を未来日付にする
- `coverImage` フィールドを新たに書く（画像取得フロー別）
- レビューエージェントを省略する
- CLAUDE-article.md を読まずに始める
