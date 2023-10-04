target = "sample/chapter08/postage.txt"

with open(target, encoding='utf-8') as f:
  for line in f:
    text = line.strip()
    if text.startswith('50g'):
      words = text.split() # 配列にする
      words.append('手紙') # 要素を追加
      text2 = ':'.join(words) # 繋げる
      print(text2)
    if text.endswith('郵便物') or text.endswith('規格外'):
      print(text)


