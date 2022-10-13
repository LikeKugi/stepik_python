"""
Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену.
Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке,
каждый на отдельной строке, в формате username@domain.
"""

emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
ziped = list()
for domain, adresses in emails.items():
    for adress in adresses:
        ziped.append(adress+'@'+domain)

print(*sorted(ziped),sep='\n')