"""
На вход программе подается число n.
Напишите программу, которая возвращает указанную строку треугольника Паскаля в виде списка
(нумерация строк начинается с нуля).
"""
from math import factorial as fc
n = int(input())

def create_pascal(n):
    return [int(fc(n)/(fc(el) * fc(n - el))) for el in range(n+1)]

for i in range(n):
    print(*create_pascal(i))

