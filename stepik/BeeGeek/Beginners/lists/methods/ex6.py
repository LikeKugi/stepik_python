"""
На вход программе подается натуральное число n≥2, а затем n целых чисел.
Напишите программу, которая создает из указанных чисел список,
состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
"""

numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
for i in range(len(numbers)-1):
    numbers[i] += numbers[i+1]
del numbers[-1]
print(numbers)