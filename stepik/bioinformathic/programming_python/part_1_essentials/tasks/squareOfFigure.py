'''
написать программу, на вход которой подаётся тип фигуры
и соответствующие параметры, которая бы выводила площадь
получившейся фигуры.
Для числа π используют значение 3.14.
'''
import math

figure = input()

if (figure == 'треугольник'):
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(S)
elif (figure == 'прямоугольник'):
    a = int(input())
    b = int(input())
    print(float(a * b))
elif (figure == 'круг'):
    r = int(input())
    print(3.14 * (r ** 2))
