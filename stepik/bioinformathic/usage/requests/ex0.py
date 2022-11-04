import requests

res = requests.get('https://docs.python.org/3.5/_static/py.png')
print(res.status_code)
print(res.headers['content-type'])

print(res.content)

with open('_ex0.png', 'wb') as ouf:
    ouf.write(res.content )


rr = requests.get('https://www.google.com/search', params={'q':'Stepic', 'oq':'stepic'})
print(rr.status_code)
print(rr.headers)
print(rr.url)
print(rr.text)