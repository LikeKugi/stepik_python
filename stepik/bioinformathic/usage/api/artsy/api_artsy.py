import requests
import json
import time


with open('tokens.txt') as tf:
    client_id = tf.readline().rstrip()
    client_secret = tf.readline().rstrip()

# # инициируем запрос на получение токена
# r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })
#
# # разбираем ответ сервера
# j = json.loads(r.text)
#
# # достаем токен
# token = j["token"]
#
# # создаем заголовок, содержащий наш токен
# headers = {"X-Xapp-Token" : token}
# # инициируем запрос с заголовком
# r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)
# r.encoding = 'utf-8' # ЭТО ОЧЕНЬ ВАЖНОЕ ДОПОЛНЕНИЕ !!!
#
# # разбираем ответ сервера
# j = json.loads(r.text)
# print(j)


with open('dataset_24476_4 (4).txt') as inf:
    name_ids = list(map(str.rstrip, inf.readlines()))

print(name_ids)
responses = []
for name in name_ids:
    time.sleep(0.4)
    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    # разбираем ответ сервера
    j = json.loads(r.text)

    # достаем токен
    token = j["token"]

    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": token}
    # инициируем запрос с заголовком
    r = requests.get(f"https://api.artsy.net/api/artists/{name}", headers=headers)
    r.encoding = 'utf-8'  # ЭТО ОЧЕНЬ ВАЖНОЕ ДОПОЛНЕНИЕ !!!

    # разбираем ответ сервера
    j = json.loads(r.text)
    print(j)
    print(j['sortable_name'], j['birthday'])
    responses.append((j['birthday'], j['sortable_name']))

print(responses)

with open('out-anser.txt', 'w', encoding='utf-8') as ouf:
    for response in sorted(responses, key=lambda x: (x[0], x[1])):
        print(response[1], file=ouf)

with open('ans.txt', 'w', encoding='utf-8') as of:
    print(*sorted(responses, key=lambda x: (x[0], x[1])), sep='\n', file=of)
