import requests
bot_api = ''
api_url = f'http://numbersapi.com/43'

params = {
    'json': 'true',
}

res = requests.get(api_url, params=params)

print(res.json())

req = [
    f'https://api.telegram.org/{bot_api}/getUpdates?offset=-1',
    f'https://api.telegram.org/{bot_api}/sendMessage?chat=173901673&text=Hello!',
    f'https://api.telegram.org/{bot_api}/sendMessage?chat_id=173901673&message=Hello world!',
    f'https://api.telegram.org/{bot_api}/getMe',
    f'https://api.telegram.org/bot<token>/getUpdate'
]

for row in req:
    print(requests.get(row))