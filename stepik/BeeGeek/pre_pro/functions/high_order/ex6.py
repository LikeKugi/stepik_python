"""
Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список,
в котором каждое значение будет результатом применения переданной функции к переданному списку.
"""

def func_apply(fn, values):
    output = list()
    for value in values:
        output.append(fn(value))
    return output


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
print(func_apply(str, [1, 2, 3, 4, 5, 6]))