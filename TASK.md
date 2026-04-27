# TASK.md — 積み残しタスク一覧

## 進行中

### カバー画像 目視確認（全ジャンル）
- **状態**: sports進行中（約25/89完了）
- **作業内容**: `public/covers/*.jpg` を1枚ずつReadツールで目視確認し、mangaTitleと一致しない画像は coverImageフィールド削除 + 画像ファイル削除
- **進捗メモリ**: `/Users/yushi/.claude/projects/-Users-yushi-Documents-manga-en/memory/cover_visual_check_progress.md`
- **未完了ジャンル**: sports(残り約64枚), horror(123枚), sci-fi(119枚), slice-of-life(194枚), fantasy(202枚), action(235枚), romance(269枚)

---

## 積み残し（未着手）

### ジャンル（genreSlug）違いチェック
- **内容**: 各記事の `genreSlug` フィールドとファイルの保存フォルダが一致しているか全件確認。不一致があれば正しいフォルダに移動し、genreSlugも修正する。
- **背景**: 目視確認中に「カテゴリが設定と違う漫画がある可能性」が浮上（2026-04-27）
- **優先度**: 低（カバー目視確認完了後）

### Amazon ASIN → 直リンクへの移行
- **内容**: 全記事の Amazon リンクを検索URLから `amazon.com/dp/<ASIN>?tag=<id>` 形式に変更
- **前提**: Amazon Associates API の申請条件（直近30日10件以上の販売）を満たしてから
- **優先度**: 低
