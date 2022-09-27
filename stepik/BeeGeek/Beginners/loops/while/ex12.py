"""
Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
"""

number = [int(i) for i in input()]
for i in number:
    if i != number[0]:
        print('NO')
        break
else:
    print('YES')