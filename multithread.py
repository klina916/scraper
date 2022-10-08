from tracemalloc import start
import requests
from bs4 import BeautifulSoup
import time
import concurrent.futures

def scrape(links):

        reqsponse = requests.get(links)

        soup = BeautifulSoup(reqsponse.text, 'lxml')

        # 產生 cache page
        path = '/Users/shenghua/Documents/webscraper/scraper/cache_page/bbc.html'
        f = open(path, 'w', encoding='utf-8')
        f.write(soup.prettify())
        f.close()

        titles = soup.find_all('a', {'class': 'bbc-uk8dsi e1d658bg0'})
        urls = soup.find_all('a')

        title_list = []
        url_list = []
        tag_list = []

        for title in titles:
            title_list.append(title.getText())
            url_list.append(title.get('href'))

            sub_response = requests.get(title.get('href'))
            sub_soup = BeautifulSoup(sub_response.text, 'lxml')
            tags = sub_soup.find_all('li', {'class': 'bbc-1msyfg1 e2o6ii40'})

            for tag in tags:
                tag_list.append(tag.getText())
            
        print(title_list)
        print(url_list)
        print(tag_list)

start_time = time.time()

links = [f"https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt?page={page}" for page in range(1,4)]

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scrape,links)

end_time = time.time()
print(f'花費{end_time - start_time}秒')