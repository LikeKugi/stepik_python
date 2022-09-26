"""
Даны пять чисел a_1, a_2, a_3, a_4, a_5. Напишите программу, которая вычисляет сумму их модулей
"""

numbers = []
for i in range(5):
    numbers.append(abs(int(input())))
sum_abs = sum(numbers)
print(sum_abs)