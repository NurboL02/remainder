
import requests
from bs4 import BeautifulSoup as BS

# pip install requests bs4
URL = "https://kg.akipress.org/?from=portal&place=menu"
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
response = requests.get(URL, headers={'User-Agent': user_agent})
print(response.status_code)
print(response.text[:120])
if response.status_code == 200:
    soup = BS(response.text, "html.parser")
    news_main = soup.find('div', class_="main_news")
    print(news_main.text)
news=[]
for nw in news_main.find_all('div', class_='list-item'):
        new = {}
        new['name'] = nw.find(class_='elem').text.replace('\n', '')
        print(news)