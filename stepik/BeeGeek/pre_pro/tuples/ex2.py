# Дополните приведенный код так, чтобы он вывел произведение элементов кортежа numbers.

from functools import reduce

numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)

product = reduce(lambda x, y: x * y, numbers)

print(product)
