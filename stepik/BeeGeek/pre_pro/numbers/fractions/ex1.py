"""
аны две дроби в формате a/b.
Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и частное.

Формат входных данных
На вход программе подаются две ненулевые дроби, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести сумму, разность, произведение и частное двух дробей.
"""
from fractions import Fraction

fraction_a = input()

fraction_b = input()


a = Fraction(fraction_a)
b = Fraction(fraction_b)

print(fraction_a, '+', fraction_b, '=', a + b)
print(fraction_a, '-', fraction_b, '=', a - b)
print(fraction_a, '*', fraction_b, '=', a * b)
print(fraction_a, '/', fraction_b, '=', a / b)
