import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active

target_csv = 'sample/chapter09/store_sales.csv'
df = pd.read_csv(target_csv)
ws.append(df.columns.tolist())
for row in df.values:
  ws.append(list(row))

row_length = 1 + len(df.values)
data = Reference(ws, min_col=2, max_col=4, min_row=1, max_row=row_length)
categories = Reference(ws, min_col=1, min_row=2, max_row=row_length)

chart = BarChart()
chart.type = 'col'
chart.shape = 4
chart.grouping = 'stacked'
chart.overlap = 100
chart.title = '支店別売上（積み上げ）'
chart.x_axis.title = '支店'
chart.y_axis.title = '売上'
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

ws.add_chart(chart, 'A9')
wb.save('tmp/store_sales.xlsx')

