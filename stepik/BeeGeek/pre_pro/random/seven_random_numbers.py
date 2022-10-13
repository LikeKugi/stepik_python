"""
Напишите программу, которая с помощью модуля random генерирует 7 различных случайных чисел для лотерейного билета.
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.
"""
from random import randrange as rr
lottery = set()
while len(lottery) < 7:
    lottery.add(rr(1,50))

print(*sorted(lottery))
