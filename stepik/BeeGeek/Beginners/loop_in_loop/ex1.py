"""
Дано натуральное число n (n≤ 9).
Напишите программу, которая печатает таблицу размером  n×3
состоящую из данного числа (числа отделены одним пробелом).

Дано натуральное число n (n≤ 9).
Напишите программу, которая печатает таблицу размером n×5,
где в i-ой строке указано число i (числа отделены одним пробелом).
"""

n = int(input())

for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()

for i in range(n):
    for j in range(5):
        print(i,end=' ')
    print()