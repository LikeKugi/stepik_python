import requests
import re

page = requests.get(input())

url_pattern = re.compile(r'<a.*?href=["|\'](.*?:\/\/)?(\w.*?)([/|:].*)?["|\'].*')
links = sorted(set([link[1] for link in url_pattern.findall(page.text)]))
print(*links, sep='\n')