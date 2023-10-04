import re

item = {}
pattern = r'(?P<weight>\d+)(?P<unit>k?g)以内\s+(?P<fee>(\d{1,3},?)+)円'

target = "sample/chapter08/postage.txt"

with open(target, encoding='utf-8') as f:
  for line in f:
    match = re.search(pattern, line)
    if match is not None:
      d = match.groupdict()
      weight = int(d['weight'])
      if d['unit'] == 'kg':
        weight = weight * 1000
      fee = d['fee'].replace(',', '')
      item[item_type].update({weight: int(fee)})
    elif line != '\n':
      item_type = line.strip()
      item[item_type] = {}

  print(f"定形郵便物: {item['定形郵便物']}")
  print(f"定形外郵便物: {item['定形外郵便物']}")
  print(f"規格外: {item['規格外']}")
