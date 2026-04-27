---
description: manga cover画像を5枚チェックしてNG処理後にコンパクト
---

以下の手順で manga カバー画像の目視確認バッチを1回実行する。

## 手順

1. `/Users/yushi/.claude/projects/-Users-yushi-Documents-manga-en/memory/cover_visual_check_progress.md` を読んで現在の未着手ジャンルと進捗を確認する

2. 次の未確認ファイル5枚を `ls /Users/yushi/Documents/manga-en/public/covers/` で特定し、並列で Read ツールを使って目視確認する

3. 各画像について `mangaTitle`（スラッグから推測）と一致するか判定：
   - ✓ OK: 正しい漫画のカバー
   - NG: 別の漫画、テキストのみ、続編・スピンオフ、プレースホルダー

4. NG の画像は即処理：
   - `sed -i '' '/^coverImage:/d'` で該当 .md から coverImage フィールドを削除
   - `rm` で画像ファイルを削除

5. 結果を簡潔に報告（✓/NG のリスト）

6. メモリファイル `cover_visual_check_progress.md` の確認済みリストを更新する

7. `/compact` を実行してコンテキストを圧縮する
