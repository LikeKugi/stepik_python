"""
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число
и возвращает значение True если число является простым и False в противном случае.
"""
import math


# объявление функции
def is_prime(num):
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0 or num == 1:
        return False
    for i in range(1, math.ceil(math.sqrt(num))):
        if (num % (6 * i - 1) == 0 and (6 * i - 1) != num) or (num % (6 * i + 1) == 0 and (6 * i + 1) != num):
            return False
    return True


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))

print(is_prime(1))
print(is_prime(10))
print(is_prime(17))
