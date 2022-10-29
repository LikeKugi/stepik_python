import json

with open('Alphabet.json') as inf:
    encoding = json.load(inf)

print(encoding)

with open('Abracadabra__1_.txt', encoding='utf-8') as inf, open('decoded.txt', 'w', encoding='utf-8') as ouf:
    for line in inf.readlines():
        for char in line:
            ouf.write(str(encoding.get(char,char)))

