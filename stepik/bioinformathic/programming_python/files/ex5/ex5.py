import requests as rq

with open('dataset_3378_3.txt') as inf:
    line = inf.readline().strip().replace('\n','')
print(line)
r = rq.get(line)
while True:
    if not r.text.startswith('We'):
        print(r.text)
        r = rq.get('https://stepic.org/media/attachments/course67/3.6.3/'+r.text)
    else:
        print(r.text)
        break