"""
Даны два целых числа m и n (m > n).
Напишите программу, которая выводит все нечетные числа от mm до nn включительно в порядке убывания.
"""

m, n = int(input()), int(input())
m += 1 if m % 2 == 0 else 0
for i in range(m, n - 1, -2):
    print(i)