#  Вам нужно найти все строки, содержащиеся между тегами <code> и </code>
import requests
import re
from collections import Counter

res = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html')
print(res.status_code)
pattern = re.compile(r'<code>(.*?)</code>')

texts = sorted(re.findall(pattern, res.text))

print(texts)

print(Counter(texts))

tags = dict()
for text in texts:
    tags[text] = tags.setdefault(text, 0) + 1

print(tags)