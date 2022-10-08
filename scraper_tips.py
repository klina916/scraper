from cmath import exp
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}

response = requests.get("https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt", headers = headers, timeout = 5)

try:
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('a', {'class': 'bbc-uk8dsi e1d658bg0'})

        if title:
            result = title.getText()
            print(result)
        else:
            print('元素不存在')
    else:
        print('狀態碼非200')
except Exception as e:
    print(str(e))
