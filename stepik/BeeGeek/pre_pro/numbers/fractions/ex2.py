"""
На вход программе подается натуральное число n.
Напишите программу, которая вычисляет и выводит рациональное число, равное значению выражения: ряд обратных квадратов

"""
from fractions import Fraction

q = map(Fraction, map(lambda x: '1/' + x, map(str, [el ** 2 for el in range(1, int(input()) + 1)])))
print(sum(q))

print(sum([Fraction(1, i ** 2) for i in range(1, int(input()) + 1)]))
