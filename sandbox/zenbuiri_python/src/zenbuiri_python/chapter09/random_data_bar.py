import random
from openpyxl import Workbook
from openpyxl.formatting.rule import DataBarRule

wb = Workbook()
ws = wb.active

values = random.sample(range(100), k=20)
for i, value in enumerate(values, 1):
  col_a = ws.cell(i, 1)
  col_a.value = value

row_length = len(values)
rule = DataBarRule(
  start_type='percentile',
  start_value=10,
  end_type='percentile',
  end_value='90',
  color='0080FF',
  showValue='None',
  minLength=None,
  maxLength=None
)
ws.conditional_formatting.add(f'A1:A{row_length}', rule)

ws.title = 'データバー'
wb.save('tmp/random_data_bar.xlsx')