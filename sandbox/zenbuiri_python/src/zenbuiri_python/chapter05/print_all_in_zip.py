import zipfile

with zipfile.ZipFile('mydir.zip', 'r') as zf:
  for info in zf.infolist():
    print(info.filename)
