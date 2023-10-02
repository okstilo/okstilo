import pathlib

path = pathlib.Path('.')
for po in path.iterdir():
  if po.match('*.md'):
    print(po)
