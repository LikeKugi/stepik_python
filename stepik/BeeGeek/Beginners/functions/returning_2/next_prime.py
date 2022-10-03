"""
Напишите функцию get_next_prime(num),
которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
"""
import math


def is_prime(num):
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0 or num == 1:
        return False
    for i in range(1, math.ceil(math.sqrt(num))):
        if (num % (6 * i - 1) == 0 and (6 * i - 1) != num) or (num % (6 * i + 1) == 0 and (6 * i + 1) != num):
            return False
    return True


# объявление функции
def get_next_prime(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1


"""
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
"""
print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
