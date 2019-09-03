import requests as rq
from bs4 import BeautifulSoup
import time

BASE_URL = "https://www.google.com/search?"
QUERY_STR = "q=%s&start=%d"

custom_headers = {
  'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1;)',
}

keyword = "python"
page = 0
cnt = 0

while True:
  page = 10*cnt + 1
  print('============= %d ============='%(page))
  res = rq.get(BASE_URL + QUERY_STR%("python", page), headers=custom_headers)
  soup = BeautifulSoup(res.content, 'lxml')

  contents = soup.select('.srg > div')

  for content in contents:
    # print(content)
    top = content.select('div')[1].text
    splited_top = top.split('›')
    
    if len(splited_top) > 1:
      title = ' '.join(splited_top[1:])
      link = splited_top[0]
      desc = content('div')[4].text

      print('link: %s'%(link))
      print('title: %s'%(title))
      print('desc: %s'%(desc))
      print()
  
  cnt += 1
  time.sleep(0.3)