from bs4 import BeautifulSoup
import requests

target_selector = '#mw-content-text > div.mw-parser-output > h2'

page_data = requests.get('https://ja.wikipedia.org/wiki/Python').text
page = BeautifulSoup(page_data, 'lxml')
h2s = page.select(target_selector)

for h2 in h2s:
  print(f'h2タイトル: {h2.text}')
