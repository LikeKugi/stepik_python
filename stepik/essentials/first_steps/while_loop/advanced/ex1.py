"""
Пользователь вводит целые числа по одному в строке, последовательность оканчивается числом 0.
Все, что вводится после 0 не относится к последовательности.
Напишите программу, которая выводит сумму всех членов данной последовательности.
"""
sum = 0
while (n := int(input())) != 0:
    sum += n

print(sum)