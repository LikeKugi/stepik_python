"""
Напишите функцию mean(), которая принимает произвольное количество аргументов
и возвращает среднее арифметическое переданных в нее числовых (int или float) аргументов.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.

Примечание 2. Функция должна игнорировать аргументы всех типов, кроме int или float.
"""

def mean(*args):
    means = [el for el in args if type(el) in [int, float]]
    if len(means) == 0:
        return 0

    return sum(means)/len(means)


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))