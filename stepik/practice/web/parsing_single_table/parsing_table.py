import requests
from bs4 import BeautifulSoup

res = requests.get('https://stepik.org/media/attachments/lesson/209723/3.html')
print(res.status_code)

with open('response.txt', 'w') as ouf:
    ouf.writelines(res.text)

soup = BeautifulSoup(res.text, 'lxml')
# print(soup)
numbers = []
for tag in soup.find_all("td"):
    numbers.append(int(tag.text.strip()))

print(numbers)
print(sum(numbers))