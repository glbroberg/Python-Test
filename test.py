import requests
from bs4 import BeautifulSoup

def trade_spider(ax_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org'
        source_code = request.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = "http://buckysroom.org" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1

trade_spider(1)

# added comments for second commit test   
