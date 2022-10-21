"""
Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее.
Каждая строка файла содержит три значения, разделенные запятыми и символом пробела:
имя пользователя, время входа, время выхода, где время указано в 24-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей
(не меняя порядка следования), которые были в сети не менее часа.
"""

with open('logfile.txt', encoding='utf-8') as inf, open('output.txt', 'w', encoding='utf-8') as ouf:
    for line in inf.readlines():
        name, begin, stop = map(str.rstrip, line.split(', '))
        hh,mm = map(int, begin.split(':'))
        begin = (hh * 60 + mm)
        hh, mm = map(int, stop.split(':'))
        stop = (hh * 60 + mm)

        print(name, stop-begin)
        if stop - begin >= 60:
            print(name, file=ouf)
