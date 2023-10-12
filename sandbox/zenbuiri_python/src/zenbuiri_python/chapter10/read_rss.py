import feedparser

url = 'https://www.jma-net.go.jp/rss/jma.rss'
result = feedparser.parse(url)

print(result['feed']['title'])

for i, entry in enumerate(result['entries']):
  print(f'title: {entry.get("title")}')
  print(f'link: {entry.get("link")}')
  print(f'published: {entry.get("published")}')
  print(f'summary: {entry.get("summary")}')
  print()

  if i > 9:
    break





