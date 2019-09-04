import requests as rq
from bs4 import BeautifulSoup
import time

class Google:

  def __init__(self):
    self.BASE_URL = "https://www.google.com/search?"
    self.QUERY_STR = "q=%s&start=%d"

    self.custom_headers = {
      'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1;)',
    }

    self.keyword = "python"
    self.page = 0
    self.cnt = 0

  def crawler(self):
    self.page = 10 * self.cnt + 1
    
    print('============= %d ============='%(self.page))

    res = rq.get(
      self.BASE_URL + self.QUERY_STR%("python", self.page), 
      headers=self.custom_headers
    )
    soup = BeautifulSoup(res.content, 'lxml')
    contents = soup.select('.srg > div')

    temp = []

    for content in contents:
      top = content.select('div')[1].text
      splited_top = top.split('›')
      
      if len(splited_top) > 1:
        title = ' '.join(splited_top[1:])
        link = splited_top[0]
        desc = content('div')[4].text

        temp.append({
          'link': link,
          'title': title,
          'desc': desc
        })
    
    self.cnt += 1
    return temp

if __name__== "__main__":
  google = Google()

  while True:
    result = google.crawler()

    for item in result:
      print('link: %s'%(item["link"]))
      print('title: %s'%(item["title"]))
      print('desc: %s'%(item["desc"]))
      print()
    time.sleep(0.3)