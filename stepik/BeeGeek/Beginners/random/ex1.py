import math
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)  # принимает список в качестве обязательного аргумента и перемешивает его случайным образом.
print(numbers)

print(random.choice(
    'BEEGEEK'))  # принимает список (строку) в качестве обязательного аргумента и возвращает один случайный элемент
print(random.choice([1, 2, 3, 4]))
print(random.choice(['a', 'b', 'c', 'd']))

numbers = [2, 5, 8, 9, 12]
"""
принимает два обязательных аргумента: список (строку) и количество случайных элементов, 
а возвращает список случайных элементов в указанном количестве.
"""
print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))


num = 20
print(math.log2(num))