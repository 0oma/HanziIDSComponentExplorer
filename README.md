[繁體中文](#漢字-ids-部件查詢) | [English](#hanzi-ids-component-explorer)

---

# 漢字 IDS 部件查詢

[Glyphs](https://glyphsapp.com/) 字型編輯器外掛，用於拆解漢字結構並查詢相關字符。

<p align="center">
  <img src="screenshot.png" alt="截圖" width="500">
</p>


## Hanzi Component Explorer

この封裝版は v1.4.1 を起点に、右ペインの文字タイルと制作済みグリフ確認をさらにリッチにした 版 です。

- **ステータス付き文字タイル** — 右側の関連字を `●字` / `○字` / `–字` / `★字` のような状態付きタイルとして表示します。
- **タイル密度切替** — コンパクト・標準・ゆったりの3段階で、関連字の見え方を切り替えられます。
- **制作進捗の常時表示** — サマリーに `●制作済み / ○グリフあり / –未作成 / ★お気に入り` の数と制作済み率を表示します。
- **一覧プレビューバッジ** — 中央リスト上で `●` 制作済み、`○` グリフあり未作成、`–` 未作成を確認できます。
- **制作済みグリフプレビュー** — 左側プレビューは、Glyphs の現在フォント内にアウトラインがある場合、そのレイヤーを画像として描画します。
- **プレビュー情報の整理** — 左ペインに Unicode と画数を追加し、制作状態との対応を見やすくしました。
- **カード型UI** — サマリー、プレビュー、詳細、分解リスト、関連字ペインを角丸カード風に整理しました。
- **検索履歴・お気に入り・一括操作** — 最近の検索、★お気に入り、関連字だけコピー、関連字だけ一括挿入を追加しています。
- **独立設定キー** — 版 版の bundle id / defaults prefix を分離し、原版と設定が干渉しにくい構成です。

## 功能

- **字符拆解** — 輸入漢字，視覺化顯示其部件樹狀結構
- **多部件組合搜尋** — 輸入多個部件（如「氵木」）找出同時包含所有部件的字；採遞迴比對（部件藏在更深層也算，如「淋」含「木」），可再拆的中間部件也能當查詢詞（如「立里」找到「童」、「火林」找到「焚」），重複部件代表「至少 N 個」（如「木木」找含兩個以上木的字）
- **同字根查詢** — 找出與本字結構相同的關聯字
- **衍生字查詢** — 找出以本字為部件的衍生字
- **字集篩選** — 預設顯示字型檔內的字，亦可使用自訂字集
- **顏色篩選** — 依 Glyphs 顏色標籤過濾結果
- **筆畫數篩選** — 用底部滑桿選擇 ±0/±1/±2/±3/±5 筆畫差，快速從相關字中找到筆畫接近主字的造字參考（資料源自 CNS11643）
- **全字庫連結** — 一鍵查詢 CNS11643 全字庫資料

## 安裝

### 外掛程式管理員（推薦）

1. *視窗 > 外掛程式管理員*
2. 搜尋「HanziIDSComponentExplorer」
3. 點擊 *安裝*
4. 重新啟動 Glyphs

### 手動安裝

下載 `HanziIDSComponentExplorer.glyphsPlugin`，雙擊安裝。

## 使用方式

1. *視窗 > 漢字 IDS 部件查詢* 開啟視窗
2. 在搜尋欄輸入漢字（如「森」）或 Unicode（如「68EE」）
3. 查看拆解結果、同字根、衍生字
4. 輸入多個部件（如「氵木」）搜尋同時包含所有部件的字：中欄列出輸入部件、右欄列出符合的字；此時筆畫篩選以各部件筆畫加總為基準（如「氵木」= 7 畫）

## 系統需求

- Glyphs 3.0 或以上
- macOS 10.9 或以上

## 資料來源

- **IDS 拆解資料** — [CHISE IDS database](https://www.chise.org/ids/) 的 CNS 及 Unicode 資料，收錄超過 10 萬個字符
- **筆畫數資料** — [CNS11643-OpenData](https://github.com/yintzuyuan/CNS11643-OpenData) 的 `Tables/Properties/CNS_stroke.txt`，覆蓋約 7.7 萬字（74.8%）。超出 CNS 範圍的 Ext-G/H 罕字筆畫為空，僅在「關閉筆畫篩選」時顯示

## 授權

程式碼以 [Apache License 2.0](LICENSE) 授權。

本外掛內含的 `ids.pdata` 為 [CHISE IDS](https://www.chise.org/ids/) 衍生資料，受 [GPL-2.0-or-later](LICENSES/GPL-2.0-or-later.txt) 約束。CNS11643 資料依[政府資料開放授權條款](https://data.gov.tw/license)使用。

詳見 [NOTICE](NOTICE)。

## 作者

**殷慈遠 TzuYuan Yin** — [erikyin.net](https://erikyin.net)

## 致謝

- [CHISE Project](https://www.chise.org/) — IDS 資料庫
- [全字庫](https://www.cns11643.gov.tw/) — 字形資料參考
- [3type/EOD 拆字小組](https://github.com/3type/EOD) — 資料格式啟發

---

# Hanzi IDS Component Explorer

A [Glyphs](https://glyphsapp.com/) font editor plugin for decomposing Chinese characters and exploring related glyphs.

<p align="center">
  <img src="screenshot.png" alt="Screenshot" width="500">
</p>


## Hanzi Component Explorer

This packaged 版 starts from v1.4.1 and further enriches the character-tile and in-font production preview workflow.

- **Status-badged character tiles** — related characters are rendered as `●char` / `○char` / `–char` / `★char` tiles.
- **Tile density control** — cycle between Compact, Comfortable, and Spacious tile layouts.
- **Always-visible production stats** — the summary area shows counts for `● designed`, `○ glyph exists`, `– missing`, `★ favorite`, plus designed percentage.
- **Modern connected decomposition tree** — the middle decomposition list uses compact connected tree branches and keeps status badges at the row end so branch alignment remains clean.
- **List preview badges** — the middle decomposition list shows `●` designed, `○` glyph exists but empty, and `–` missing.
- **Designed glyph preview** — when the current Glyphs font has outlines for a character, the left preview draws that actual layer as an image.
- **Cleaner preview metadata** — Unicode and stroke count are shown directly under the preview status.
- **Card-style interface** — the summary, preview, details, decomposition list, and related-character panes are visually separated.
- **History, favorites, and bulk actions** — recent searches, ★ favorites, characters-only copy, and bulk insert are included.
- **Isolated 版 settings** — bundle id and defaults prefix are separated from the upstream plugin.




## v1.6.4 Clean UI

- 右ペインのタイル表示をウィンドウ幅に合わせて自動折り返しするように調整
- 選択タイルの右クリックメニューを追加
  - 新規タブで開く
  - 現在タブに挿入
  - 文字コピー
  - Unicodeコピー
  - 先頭字を検索
  - お気に入りへ追加/削除
- フィルターに「制作済みのみ表示」を追加
- 上部サマリーと左プレビューのステータス表示を整理

## v1.6.2 樹形図表示

- 既存のテキスト樹形図を確認し、`HanziCore.decompose()` の出力をコンパクトな接続型ツリーへ整理
- 深層分解時も `│ / ├─ / └─` の枝が途切れにくいよう、親階層ごとの継続線を計算
- 中央一覧の制作ステータスバッジを行頭から行末へ移し、枝の開始位置を揃えた
- 中央一覧は可能なら等幅システムフォントを使い、枝線の視認性を改善
- 文字抽出処理は新しい枝記号と `● / ○ / – / ★` を無視するよう更新

## v1.6.1 Clean UI / Status Refactor

- ステータス判定を `glyph_status.py` に分離し、一覧・タイル・サマリーの `● / ○ / – / ★` 表示を同じ判定に統一
- Glyphsのグリフ状態取得を表示更新ごとにキャッシュし、右ペインの大量タイル表示で同じ文字の判定を繰り返しにくくした
- 上部サマリーを「焦点字情報」「字集合/関連字数」「表示モード」「総数/選択/進捗」に整理
- タイルON/OFF、密度、タイル内グリフプレビュー、一覧バッジ状態を常時見えるステータス行に移動
- 右ペインの総数・選択数・お気に入り数・制作済み率を常時表示
- タイル表示 の選択・ダブルクリック挙動は v1.6.0 の仕様を維持

## v1.6.0 タイル表示 追加

この版では、右ペインのタイル表示を `NSTextView` の装飾テキストから分離し、独自のタイルオブジェクト描画エンジンに置き換えています。

- **オブジェクトタイル選択** — クリックで単体選択、Shift/Commandクリックで複数選択。クリックで選択が崩れる問題を回避
- **ダブルクリック展開** — 選択中の単体/複数タイルを新規 Glyphs タブで展開
- **リッチなステータス表示** — `★` お気に入り、`●` 制作済み、`○` グリフあり、`–` 未作成をタイル内バッジとして描画
- **タイル内グリフプレビュー** — オプションON時、制作済みグリフはタイル内に実アウトラインの小プレビューを表示
- **テキスト表示フォールバック** — カスタムビュー生成に失敗した場合やタイル表示OFF時は従来のテキスト表示へ戻る

## Features

- **Character Decomposition** — Visualize the component tree structure of any Chinese character
- **Multi-Component Search** — Enter multiple components (e.g. "氵木") to find characters containing all of them; uses recursive matching (a component nested deeper still counts, e.g. "淋" contains "木"), decomposable intermediate components also work as queries (e.g. "立里" finds "童", "火林" finds "焚"), and repeated components mean "at least N" (e.g. "木木" finds characters with two or more 木)
- **Sister Characters** — Find characters sharing the same structure
- **Derived Characters** — Find characters using this character as a component
- **Charset Filtering** — Filter by current font glyphs or custom charset
- **Color Filtering** — Filter by Glyphs color labels
- **Stroke Count Filtering** — Discrete bottom slider (±0/±1/±2/±3/±5) to narrow related characters by stroke count difference from the current character (data from CNS11643)
- **CNS Link** — Quick lookup in CNS11643 database

## Installation

### Plugin Manager (Recommended)

1. *Window > Plugin Manager*
2. Search for "HanziIDSComponentExplorer"
3. Click *Install*
4. Restart Glyphs

### Manual Installation

Download `HanziIDSComponentExplorer.glyphsPlugin` and double-click to install.

## Usage

1. Open *Window > Hanzi Component Explorer*
2. Enter a Chinese character (e.g., "森") or Unicode (e.g., "68EE")
3. View decomposition, sister characters, and derived characters
4. Enter multiple components (e.g. "氵木") to find characters containing all of them: the middle column lists the input components, the right column lists the matches; stroke filtering then uses the sum of the components' stroke counts as the baseline (e.g. "氵木" = 7 strokes)

## Requirements

- Glyphs 3.0+
- macOS 10.9+

## Data Sources

- **IDS decomposition** — [CHISE IDS database](https://www.chise.org/ids/) (CNS and Unicode), covering over 100,000 characters
- **Stroke counts** — `Tables/Properties/CNS_stroke.txt` from [CNS11643-OpenData](https://github.com/yintzuyuan/CNS11643-OpenData), covering ~77k characters (74.8%). Characters outside CNS11643 (Ext-G/H rare ideographs) have no stroke data and are only shown when stroke filtering is OFF

## License

Source code is licensed under [Apache License 2.0](LICENSE).

The bundled `ids.pdata` is derived from the [CHISE IDS](https://www.chise.org/ids/) database and is subject to [GPL-2.0-or-later](LICENSES/GPL-2.0-or-later.txt). CNS11643 data is used under the [Open Government Data License, Taiwan](https://data.gov.tw/license).

See [NOTICE](NOTICE) for details.

## Author

**TzuYuan Yin** — [erikyin.net](https://erikyin.net)

## Acknowledgments

- [CHISE Project](https://www.chise.org/) — IDS database
- [CNS11643 全字庫](https://www.cns11643.gov.tw/) — Glyph data reference
- [3type/EOD](https://github.com/3type/EOD) — Data format inspiration

---

Copyright 2026 TzuYuan Yin
