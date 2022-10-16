"""
На вход программе подается натуральное число n.
Напишите программу, которая выводит в порядке возрастания все несократимые дроби,
заключённые между 0 и 1, знаменатель которых не превосходит n.

Формат входных данных
На вход программе подается натуральное число n, n>1.
"""
from fractions import Fraction as FF
from math import gcd as GCD

n = int(input())
numbers = set()
for i in range(1, n + 1):
    for j in range(1, i):
        if GCD(j,i)==1:
            numbers.add(FF(j, i))
print(*sorted(numbers),sep='\n')
