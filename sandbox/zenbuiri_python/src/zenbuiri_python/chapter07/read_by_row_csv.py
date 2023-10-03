import pandas as pd

df = pd.read_csv('sample/chapter07/item_stock.csv', encoding='utf-8', header=0)
sales = sum(df['売上数'])
for i, row in enumerate(df.values):
  print(f'{i + 1}: {row}')
print(f'売上数合計: {sales}')