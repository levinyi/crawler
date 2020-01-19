import requests
import os

url = 'https://adv-r.hadley.nz/preface.html'

from bs4 import BeautifulSoup

html = requests.get(url)
if html.status_code == 200:
    soup = BeautifulSoup(html.text, "html.parser")
    print(soup.find_all('li', {'data-level': "2"}))
    # for link in soup.find_all('li', {"class": "chapter"}):
    #     print(link)