import requests
from bs4 import BeautifulSoup

res = requests.get('https://stepik.org/media/attachments/lesson/209723/4.html')
print(f'response status: {res.status_code}')

with open('response.txt', 'w') as ouf:
    ouf.writelines(res.text)

with open('response.txt') as inf:
    data = inf.read().replace('\n', '')

soup = BeautifulSoup(data, 'lxml')
print(soup)
numbers = []
for tag in soup.find_all("td"):
    numbers.append(int(tag.text.strip()))

print(numbers)
print(sum(numbers))
