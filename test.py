import requests
from bs4 import BeautifulSoup

def trade_spider(ax_pages):
    page = 1
    while page <= max_pages:
        url = 'https://buckysroom.org'