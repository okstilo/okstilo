target = "sample/chapter08/postage.txt"

with open(target, encoding='utf-8') as f:
  for line in f:
    text = line.strip()
    print(text)
