# SQL 第2版 ゼロからはじめるデータベース操作

## 第0章　イントロダクション――SQL学習環境を作ろう

- postgresqlのインストールはbrewで実行
- 以下、本書の通りに `shop` DBを作成した


```shell
$ psql -l
                                                     データベース一覧
   名前    | 所有者 | エンコーディング | 照合順序 | Ctype(変換演算子) | ICUロケール | ロケールプロバイダー | アクセス権限
-----------+--------+------------------+----------+-------------------+-------------+----------------------+--------------
 postgres  | msk    | UTF8             | C        | C                 |             | libc                 |

```

```sql
postgres=# CREATE DATABASE shop;
CREATE DATABASE
```

```shell
$ psql -l
                                                     データベース一覧
   名前    | 所有者 | エンコーディング | 照合順序 | Ctype(変換演算子) | ICUロケール | ロケールプロバイダー | アクセス権限
-----------+--------+------------------+----------+-------------------+-------------+----------------------+--------------
 postgres  | msk    | UTF8             | C        | C                 |             | libc                 |
 shop      | msk    | UTF8             | C        | C                 |             | libc                 |
```

## 第1章　データベースとSQL

- [TablePlus](https://tableplus.com) を導入した。課金してもいいぐらい使いやすい
- SQLをサクサク書けて便利
- `Shohin` テーブルを作成した
- `Shohin` にデータ登録した
  - TablePlusは1行ずつ実行されるのでRun Allしないといけない
  - VS Codeでマルチカーソルを使いたかったのでSQL文 `list_1_6.sql` 作成した

## 第2章　検索の基本

- TablePlusの[autocomplete](https://docs.tableplus.com/query-editor/autocomplete)機能が便利
  - From句で指定するテーブル名に略称をつけると、ドット構文でカラム名がサジェストされる
- SELECT文
- 算術演算子、比較演算子
- 論理演算子

## 第3章　集約と並べ替え

- 行数 count
- 合計 sum
  - null行は含まれず計算される
- 平均値 avg
  - null行は母数に含まれず計算される
- 最大値 max, 最小値 min
- 重複値を外して集約関数を使う DISTINCT（でぃすてぃんくと）
- グループに切り分ける GROUP BY
  - nullはnullというグループで切り分けられる
  - where句と併用したときは以下の実行順序
    - from -> where -> group by -> select
  - select句に集約キー以外の列名（group byで使う列名以外）は使えない
- having 集約した結果を条件指定する
  - having句：グループに対する条件指定
  - where句：行に対する条件指定（行数を絞り込むため実行速度が速い
- 並べ替え order by
  - デフォで昇順 `ASC` 、降順は `DESC` を指定する
  - nullは先頭か末尾にまとめて表示される

### 記述順序

1. select
2. from
3. where
4. group by
5. having
6. order by

## 第4章　データの更新

- 登録 Insert
  - テーブルのコピー
  - テーブルを加工してコピー
- 削除 Delete
- 更新 update
  - トランザクション
    - COMMIT 処理の確定
      - トランザクション前に戻すことはできない
    - ROLLBACK 処理の取り消し
      - トランザクション前に戻る
  - ACID特性
    - 原始星 Atomicity
      - 実行されるか、実行さないか（オールオアナッシング）
    - 一貫性 Cisistency
      - 必ず整合性を保つ
    - 独立性 Isolation
      - 他から干渉を受けることがない
    - 永続性 Durability

## 第5章　複雑な問い合わせ

### ビュー

- Viewは仮想テーブル
  - `group by` は使えない
  - 仮想なので `Insert` などの更新はできない

### サブクエリ

- サブクエリは使い捨てのビュー
  - FROM句の中にネストして使い捨ての名前をつける
- スカラ・サブクエリ
  - 必ず1行1列だけの戻り値を返す
  - select ~ from をネストする

### 相関サブクエリ

- 小分けにしたグループ内での比較をするときに使う
  - FROM で AS を使う（TablePlusでは略称を使う）
  - where句で結合条件を書く
- サブクエリではできなかったことができる

## 第6章　関数、述語、CASE式

- いろいろな関数
  - 算術関数
    - 四則演算
    - ABS 絶対値
    - MOD 剰余
    - ROUND 四捨五入
  - 文字列関数
    - || 連結
    - LENGTH 文字列長
    - LOWER/UPPER 小文字化/大文字化
    - REPLACE 置換
    - SUBSTRUNG 切り出し
  - 日付関数
    - CURRENT_DATE 日付
    - CURRENT_TIME 時間
    - CURRENT_TIMESTAMP 日時
    - EXTRACT 日付の切り出し
  - 変換関数
    - CAST 型変換
    - COALESCE（コアレス）Nullを値へ変換
  - 集約関数
    - COUNT, SUM, AVG, MAX, MIN
- 述語
  - LIKE 文字列の部分一致
    - 前方一致、中間一致、後方一致
  - BETWEEN 範囲検索
    - 以上以下（指定した値も含む）
  - IS NULL, IS NOT NULL NULL判定
  - IN ORの省略形
    - IN (1, 20, 300) いずれかが含むか
    - INの条件にサブクエリを含ませる
  - EXISTS（イグジスツ）
    - ある条件に一致するものがあるかどうか
- CASE式
  - プログラミングのSwitch文のようなもの
  - まとめて AS で名付けて出力することもできる

## 第7章　集合演算

###　集合演算

- UNION テーブル同士のたし算
- INTERSECT 共通部分
- EXCEPT テーブル同士の引き算

###　結合

- INNER JOIN 内部結合
  - FROM句でテーブルの略称をつける
  - ON句で結合する
  - SELECT句で略称を使ったカラムを指定する
- OUTER JOIN 外部結合
  - やりかたは内部結合と同じ
  - どちらのテーブルを主（マスタ）とするか
    - RIGHT 右側か　LEFT 左側か
  - マスタのテーブルの情報がすべて出力される
- CROSS JOIN クロス結合
  - 全部の組み合わせが出る
  - （ほとんどつかわれない）

## 第8章　SQLによる高度な処理



## 第9章 アプリケーションからデータベースへ接続する

省略

## 付録　練習問題の解答

省略
