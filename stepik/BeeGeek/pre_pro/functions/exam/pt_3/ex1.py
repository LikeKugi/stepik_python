"""
Напишите функцию concat(), принимающую переменное количество аргументов и объединяющую их в одну строку
через разделитель (sep). Если разделитель не задан, им служит пробел.

Примечание 1. Обратите внимание, что функция concat() должна принимать не список,
а именно переменное количество аргументов.
"""


def concat(*args, sep=' '):
    return sep.join([str(el) for el in args])


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
