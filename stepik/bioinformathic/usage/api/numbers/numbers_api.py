import requests
import time

n = None
api_url = f'http://numbersapi.com/{n}/math'

params = {
    'json': 'true',
}

# res = requests.get(api_url, params=params)
# print(res.status_code)
#
# data = res.json()
# print('Interecting' if data['found'] else 'Boring')


with open('dataset_24476_3 (8).txt') as inf:
    numbers = map(str.rstrip, inf.readlines())

with open('out_answer.txt','w',encoding='utf-8') as ouf:
    for number in numbers:
        time.sleep(0.5)
        n = number
        print(n)
        api_url = f'http://numbersapi.com/{n}/math?json=true'
        print(api_url)

        res = requests.get(api_url)
        data = res.json()
        print(data['found'])
        print('Interesting' if data['found'] else 'Boring',file=ouf)