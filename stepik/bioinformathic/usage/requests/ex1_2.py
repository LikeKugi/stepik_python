
import requests
import re


START_PAGE = input()
req = requests.get(START_PAGE)
pattern = re.compile(r'''<a[^>]*?href=['"](.*?)['"][^>]*?>''')
links = re.findall(pattern, req.text)
out_links = set()
for link in links:
    if link[0].isalpha():
        link = link.replace('ftp://','').replace('http://','').replace('https://','').replace(':','/')
        if link.find('/') > -1:
            out_links.add(link[:link.find('/')])
        else:
            out_links.add(link)

print(*sorted(out_links),sep='\n')