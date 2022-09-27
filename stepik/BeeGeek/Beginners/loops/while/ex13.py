"""
Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр
при просмотре справа налево упорядоченной по неубыванию.
"""

digits = [int(i) for i in input()]
digits.reverse()
for i in range(1,len(digits)):
    if digits[i] < digits[i-1]:
        print('NO')
        break
else:
    print('YES')