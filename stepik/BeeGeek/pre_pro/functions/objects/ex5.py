"""
Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.

Список возможных функций:

квадрат: функция принимает число и возвращает его квадрат;
куб: функция принимает число и возвращает его куб;
корень: функция принимает число и возвращает корень квадратный из этого числа;
модуль: функция принимает число и возвращает его модуль;
синус: функция принимает число (в радианах) и возвращает синус этого числа.
Формат входных данных
На вход программе подается целое число и название функции, записанные на отдельных строках.
"""
import math


def calc_number(op: str):
    operations = {
        "квадрат": lambda x: x ** 2,
        "куб": lambda x: x ** 3,
        "корень": lambda x: x ** 0.5,
        "модуль": lambda x: abs(x),
        "синус": lambda x: math.sin(x)
    }

    def calcing(n):
        return operations.get(op)(n)

    return calcing


n = int(input())
operation = input()

calc = calc_number(operation)

print(calc(n))