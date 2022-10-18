"""
Напишите функцию arithmetic_operation(), которая принимает символ одной из четырех арифметических операций
(+, -, *, /) и возвращает функцию двух аргументов для соответствующей операции.
"""


def arithmetic_operation(operation):
    return lambda x, y: eval(f'{x}{operation}{y}')


add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))
