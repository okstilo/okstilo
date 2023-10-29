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


### 相関サブクエリ




## 第6章　関数、述語、CASE式



## 第7章　集合演算



## 第8章　SQLによる高度な処理



## 第9章 アプリケーションからデータベースへ接続する



## 付録　練習問題の解答


