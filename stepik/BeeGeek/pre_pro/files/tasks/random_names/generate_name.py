"""
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 3 случайные пары имя + фамилия,
а затем выводит их, каждую на отдельной строке.
"""
from random import randrange as rr

with open('first_names.txt') as f_name, open('last_names.txt') as l_name:
    names = list(map(str.rstrip, f_name.readlines()))
    lasts = list(map(str.rstrip, l_name.readlines()))

current_names = []
used_names = set()
used_lasts = set()

while len(current_names) < 3:
    name = names[rr(len(names))]
    if name not in used_names:
        used_names.add(name)

    last_name = lasts[rr(len(lasts))]
    if last_name not in used_lasts:
        used_lasts.add(last_name)

    current_names.append(name + ' ' + last_name)


print(*current_names,sep='\n')

