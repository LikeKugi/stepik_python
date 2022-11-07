from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://ru.wikipedia.org/wiki/python').read().decode('utf-8')
s = str(html)


soup = BeautifulSoup(html, 'html.parser')
for a in (soup.find_all('a',href=True)):
    print(a['href'])