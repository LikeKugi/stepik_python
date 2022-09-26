"""
Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения
"""
import math

a, b, c = float(input()), float(input()), float(input())
discr = b ** 2 - (4 * a * c)

roots = []
if discr > 0:
    roots.append((-b + math.sqrt(discr)) / (2 * a))
    roots.append((-b - math.sqrt(discr)) / (2 * a))
    roots.sort()
    print(*roots, sep='\n')
elif discr == 0:
    roots.append(-b / (2 * a))
    print(*roots)
else:
    print('Нет корней')
