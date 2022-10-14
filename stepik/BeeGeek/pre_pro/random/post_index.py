"""
Почтовый индекс в Латверии имеет вид:
LetterLetterNumber_NumberLetterLetter, где
Letter – заглавная буква английского алфавита,
Number – число от 0 до 99 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random
генерирует и возвращает случайный корректный почтовый индекс Латверии.
"""

import random as rd
import string
from random import randrange as rr


def generate_index():
    return str(
        chr(rr(65, 91)) + chr(rr(65, 91)) + str(rr(0, 100)) + '_' + str(rr(0, 100)) + chr(rr(65, 91)) + chr(rr(65, 91)))


print(generate_index())
