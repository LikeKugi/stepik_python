"""
Напишите программу для определения, является ли число произведением двух чисел из данного набора,
выводящую результат в виде ответа «ДА» или «НЕТ».
"""

divigers = list()
for _ in range(int(input())):
    divigers.append(int(input()))
number = int(input())
for diviger in divigers:
    if diviger == 0:
        continue
    d = number / diviger
    if (d in divigers) and (d != diviger) or (d in divigers) and (divigers.count(d)>1):
        print('ДА')
        break
else:
    print('НЕТ')
