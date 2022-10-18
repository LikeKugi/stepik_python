"""
Напишите функцию pretty_print(), которая выводит содержимое списка с рамкой.

Функция должна получать на вход один обязательный аргумент data – список,
который следует вывести и два необязательных строковых односимвольных  аргумента
side и delimiter и выводить содержимое списка в соответствии с примерами.

В случае если отсутствует аргумент side, то полагаем
side='-', а если отсутствует аргумент delimiter, то полагаем delimiter='|'
"""


def pretty_print(data, side='-', delimiter='|'):
    line = str(delimiter + ' ' + (' ' + delimiter + ' ').join([str(el) for el in data]) + ' ' + delimiter)
    print(' ' + side * (len(line) - 2))
    print(line)
    print(' ' + side * (len(line) - 2))


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
