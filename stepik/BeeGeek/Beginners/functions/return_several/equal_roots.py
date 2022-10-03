"""
Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа
a, b, c – коэффициенты квадратного уравнения ax^2+bx+c = 0
и возвращает его корни в порядке возрастания.
"""
import math


# объявление функции
def solve(a, b, c):
    discr = b ** 2 - (4 * a * c)
    if discr >= 0:
        return min(((-b + math.sqrt(discr)) / (2 * a)), ((-b - math.sqrt(discr)) / (2 * a))), max(
            ((-b + math.sqrt(discr)) / (2 * a)), ((-b - math.sqrt(discr)) / (2 * a)))


print(solve(1, -4, -5))
print(solve(-2, 7, -5))
print(solve(1, 2, 1))
