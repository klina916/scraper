import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}

reqsponse = requests.get("https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt", headers=headers)

soup = BeautifulSoup(reqsponse.text, 'lxml')

# 產生 cache page
path = '/Users/shenghua/Documents/webscraper/scraper/cache_page/bbc.html'
f = open(path, 'w', encoding='utf-8')
f.write(soup.prettify())
f.close()

titles = soup.find_all('a', {'class': 'bbc-uk8dsi e1d658bg0'})

title_list = []
for title in titles:
    title_list.append(title.getText())
    print(title.getText())
    
print(title_list)

