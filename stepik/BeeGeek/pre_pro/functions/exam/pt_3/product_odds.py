"""
Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().
"""
from functools import reduce


def product_of_odds(data):  # data - список целых чисел
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2 != 0, data), 1)
