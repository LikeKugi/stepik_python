"""
Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
"""


numbers = []
while sum != 0:
    if len(numbers) == 0:
        sum = 0
    numbers.append(int(input()))
    sum += numbers[-1]
sum = 0
for i in numbers:
    sum += i**2
print(sum)