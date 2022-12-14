import random

# shuffle() принимает список в качестве обязательного аргумента и перемешивает его случайным образом

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)

# choice() принимает список (строку, кортеж) в качестве обязательного аргумента и возвращает один случайный элемент

print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(('a', 'b', 'c', 'd')))

# sample() принимает два обязательных аргумента:
# первый – список (строка, кортеж, множество),
# второй – количество случайных элементов

numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))

# string раньше использовался для расширения стандартных возможностей (функционала) строкового типа
# в модуле string остались удобные константные строки, которые можно использовать при решении задач.

import string

print(string.ascii_letters)     # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_uppercase)   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)   # abcdefghijklmnopqrstuvwxyz
print(string.digits)            # 0123456789
print(string.hexdigits)         # 0123456789abcdefABCDEF
print(string.octdigits)         # 01234567
print(string.punctuation)       # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.printable)         # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
                                # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c