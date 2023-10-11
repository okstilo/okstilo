import time
from pathlib import Path
from bs4 import BeautifulSoup
import requests

output_folder = Path('tmp/hunting_cats')
output_folder.mkdir(exist_ok=True)

target_url = 'https://commons.wikimedia.org/wiki/Category:Hunting_cats'

page_data = requests.get(target_url).text
page = BeautifulSoup(page_data, 'lxml')

for i, img in enumerate(page.select('img')):
  src = img.attrs['src']

  splited_src = src.split('/')
  img_name = splited_src[-1]
  img_path = str(i +1) + "_" + img_name

  print(f"No. {i}: {img_name}")

  save_path = output_folder.joinpath(img_path)
  image = requests.get(src)
  open(save_path, 'wb').write(image.content)
  time.sleep(1.0)

  if i > 10:
    break


