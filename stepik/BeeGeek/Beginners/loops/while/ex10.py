"""
Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
"""
from functools import reduce

digits = input()
total = reduce(lambda a, y: int(a) + int(y), digits)
print(total)
print(len(digits))
total_multyply = reduce(lambda a, y: int(a) * int(y), digits)
print(total_multyply)
print(total/len(digits))
print(digits[0])
print(int(digits[0])+int(digits[-1]))
