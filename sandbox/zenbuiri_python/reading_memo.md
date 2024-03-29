#　できる 仕事がはかどるPython自動処理 全部入り。

## Chapter 1　Pythonのプログラムを利用する前に

PythonのインストールとVS Codeの設定など

## Chapter 2　コマンドラインインターフェース

主にPowerShellの使い方。Windowユーザ向けに書かれており関係なさそうなのでパス

## Chapter 3　サードパーティライブラリのインストール

`pip` や `conda` を使ってライブラリのインストールのやり方などの説明。関係ないのでパス

## Chapter 4　Pythonのおさらい

Pythonの基本的な使い方などの説明

## Chapter 5　ファイルの操作と圧縮・展開

Pythonの `zipfile` を使ってZipファイルの圧縮・解答をやる
`src/chapter05` にサンプルファイルを写経した

## Chapter 6　画像の加工

- [ ] Pillow（ `PIL` ）を使って画像を扱うやり方

## Chapter 7　CSVファイルの処理

- `pandas` を使ってCSVの読み込み書き込み
- jsonからcsvへの変換
- あと、細々としたところの説明

## Chapter 8　テキストデータの処理

- textの読み出しと加工
- 正規表現の使い方
  - htmlタグを取り除く
- PDFからテキスト抽出
  - アウトラインの抽出
  - 本文の抽出
- Markdown形式のドキュメントをHTMLに変換する
  - `markdown2` を入れる
- [x] テキストから重要語句を抜き出す
  - `janome` を入れる
  - 形態素解析によって名詞などの単位で言葉を抜き出すことができる
  - 抜き出した言葉を何個含まれているかなどの解析ができる

## Chapter 9　Microsoft Excelとの連携

- `openpyxl` を導入した
- ワークブック、ワークシート、セルのそれぞれの読み込みした
- CSVを読み込んでグラフを作成する
- 条件付き書式
  - ランダムなデータバーを作成する
  - 条件式を使って作成する
    - python側で条件をいれる
    - Excelの条件をPythonの中に入れる

## Chapter 10　Webスクレイピング

- WEBページが要素を取り出す
  - 例題のimpressのページはSSLが通らなかったのでWikipediaで試した
- 画像を取得
  - alt属性がなかったので、適当に番号をつけて保存した
  - imgの保存方法がおかしいのかDLされたものはプレビューで表示できなかった
- WEBブラウザを操作
  - 対話モードでChromeを起動してYahooにアクセスできた
  - Chromeでアクセスした先のCSSを指定してスクショを保存できた
    - 一部、メソッドが変わっていたので対応した
- RSSフィードを受信
  - 気象庁のニュースのサマリーを取得した。簡単で便利な感じがした

```python
>>> from selenium import webdriver
>>> driver = webdriver.Chrome()
>>> driver.get("https://www.yahoo.co.jp")
```

## Chapter 11　Web API

Googleの認証周りがめんどくさそうなので、使えるところを読むだけにした


以上。