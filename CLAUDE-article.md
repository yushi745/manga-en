# 単一タイトル記事ルール

→ 1作品1記事（レビュー記事）の執筆ルール。まとめ記事・ガイド記事は CLAUDE-guide.md を参照。

---

## 事前調査

**新規記事**
- WebFetchで日本語ソース（Wikipedia・ニコニコ大百科・ファン考察サイト）を複数参照する
- 目的: キャラ名・台詞・章の転換点・結末の構造など「その作品でしか書けない事実」を収集する
- Search Consoleデータは存在しないためスキップ

**リライト**
- `data/search-console/performance-2026-05-17/` でそのスラッグのクエリを確認する
- 上位クエリに答えるH2セクションを記事内に追加する（例: "why is punpun drawn as a bird" → セクション追加）
- WebFetchも実施する
- frontmatterに `rewritten: "YYYY-MM-DD"` を追加する

---

## セクション構成

### 必須（全記事）

1. **frontmatter**
   - titleのサブタイトルは「逆説・核心・意外性」を1フレーズで
   - 良い例: "A Basketball Manga Where Effort Doesn't Beat Reality"
   - 悪い例: "The Basketball Manga That Never Gives Up"（説明的すぎる）

2. **冒頭フック**（見出しなし・frontmatter直後）
   - Yuの個人的な記憶・体験から始める。読者がYuという人間を感じられる1〜3段落
   - 「問い」だけで始めるのは禁止

3. **## Quick Take**（3行箇条書き）
   - 3番目の箇条書きに必ずageRatingを明記する

4. **## Story Overview**
   - 序盤・転換点・結末の構造まで書く。「概要」で終わらせない
   - 「ネタバレになるから書かない」は禁止

5. **## Characters**
   - 各キャラクターの「実際のアーク」を書く（性格説明だけでは不十分）
   - 例: 「アイコは転校生」ではなく「アイコは鹿児島の約束を13年間抱えたまま、種子島で死ぬ」
   - 主要キャラは最低3〜4人

6. **## What I Love About It**
   - 特定のシーン・コマ・台詞を1つ選んで深く掘り下げる（最重要セクション）
   - 「このシーンのどの要素が・なぜYuに刺さったか」を書く。最低2段落
   - 「感動した」「泣いた」で終わる文は書かない

7. **## Memorable Scene ⚠️ Spoiler Warning**
   - 何が起きたか・ページがどう見えるか・なぜ頭から離れないかを書く
   - 「〜のシーンが印象的」で終わらない。「意図的に曖昧にした」系の逃げも禁止

8. **## Pros & Cons**
   - Consの最後に「this won't work for everyone」系フレーズを1行加える
   - 例: "The pacing is slow — that's either a flaw or a feature depending on you."

9. **## Is [Manga Title] Worth Reading?**（SEO H2）
   - 検索クエリ "Is [X] worth reading?" を拾うためのセクション
   - Pros & Consを1〜2文で凝縮してまとめ直すだけでOK

10. **## Where to Buy** + FTC Disclosure
    - 固定文言は `CLAUDE-templates.md` を参照

### オプション（内容に価値があれば入れる）

- **## Who Is This Manga For?**（おすすめ読者・4項目）
- **## Content Warnings & Age Rating** ※M/18+作品は必須扱い
- **## Yu's Rating**（5軸テーブル）→ `CLAUDE-templates.md` 参照
- **## Art Style**
- **## Cultural Context**
- **## What English-Speaking Fans Say**
- **## Similar Manga**（3列テーブル必須・箇条書き禁止）→ `CLAUDE-templates.md` 参照
- **## Reading Order / Where to Start**
- **## Official English Translation Status**
- **## Format Comparison**（Physical / Digital / Omnibus）

### テンプレートの使い方

全セクションを均等に埋めない。一番語れるセクションを2倍の長さにして、薄くなるセクションは削るか短くする。200字未満のセクションは削除 or 他セクションに統合する。

---

## 自己チェックリスト（生成後・コミット前に必ず実行）

**内容の深さ**
- [ ] 冒頭フックはYuの個人的体験から始まっているか（「問い」だけで始まっていないか）
- [ ] WebFetchで収集した具体的な事実（台詞・転換点・結末）が記事に反映されているか
- [ ] Story Overviewが「概要」で終わっていないか（転換点・結末まで書いているか）
- [ ] Charactersが性格説明だけになっていないか（各キャラのアークが書かれているか）
- [ ] What I Loveが「感動した」「泣いた」で終わっていないか（特定シーン・コマを深掘りしているか）
- [ ] Memorable Sceneが「〜のシーンが印象的」で終わっていないか（具体的に描写しているか）
- [ ] 200字未満の薄いセクションが残っていないか

**フォーマット**
- [ ] Quick Takeの3番目にageRatingが明記されているか
- [ ] M/18+作品はContent Warnings冒頭にも太字で記載しているか
- [ ] Consの最後に「won't work for everyone」系フレーズがあるか
- [ ] Similar Mangaを入れた場合、3列テーブルになっているか

**frontmatter**
- [ ] `coverImage` フィールドを書いていないか（画像取得前に書いてはならない）
- [ ] `publishedAt` が未来日付になっていないか
- [ ] `mangaTitleJa` が入っているか
