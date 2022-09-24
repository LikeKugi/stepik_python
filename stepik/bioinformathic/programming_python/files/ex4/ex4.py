import requests as rq

with open('dataset_3378_2.txt') as inf:
    line = inf.readline().strip().replace('\n', '')
r = rq.get(line)
open('downloaded.txt', 'wb').write(r.content)
with open('downloaded.txt') as df:
    lines = df.read()
print(lines.count('\n'))
