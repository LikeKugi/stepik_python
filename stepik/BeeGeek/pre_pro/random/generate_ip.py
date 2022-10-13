"""
IP адрес состоит из четырех чисел из диапазона от 0 до 255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.
"""
from random import randrange as rr

def generate_ip():
    print('.'.join([str(rr(0,256)) for _ in range(4)]))

generate_ip()