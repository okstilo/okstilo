import zipfile

with zipfile.ZipFile('mydir.zip', 'w') as zf:
  zf.write('sample/chapter05/mydir1/test1.txt')
  zf.write('sample/chapter05/mydir1/test2.txt')