"""
Вам доступен текстовый файл nums.txt.
В файле могут быть записаны целые неотрицательные числа и все, что угодно.
Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая вычисляет сумму всех чисел, записанных в файле.
"""

with open('nums.txt') as inf:
    numbers = list()
    current_number = ''
    line = inf.read()
    for i in range(len(line)):
        if line[i].isdigit():
            current_number += line[i]
        elif len(current_number) > 0:
            numbers.append(int(current_number))
            current_number = ''

print(sum(numbers))
