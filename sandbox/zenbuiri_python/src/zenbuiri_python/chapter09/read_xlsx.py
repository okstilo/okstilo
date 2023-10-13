from openpyxl import load_workbook

target_file = 'sample/chapter09/various_worksheets.xlsx'
wb = load_workbook(target_file, read_only=True)

for ws in wb.worksheets:
  for row in ws:
    values = [str(column.value) for column in row]
    print(values)
