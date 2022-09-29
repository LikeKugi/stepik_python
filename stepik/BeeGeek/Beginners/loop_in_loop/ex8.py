"""
На вход программе подается два натуральных числа a и b (a < b).
Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
"""

a, b = int(input()), int(input())
max_total = 0
max_number = 0
for i in range(a, b + 1):
    total = 0
    for j in range(1, i + 1):
        if i % j == 0:
            total += j
    if total >= max_total:
        max_number = i
        max_total = total
print(max_number,max_total)
