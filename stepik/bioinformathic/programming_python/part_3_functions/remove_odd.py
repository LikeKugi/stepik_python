"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
удаляет из него все нечётные значения, а чётные нацело делит на два.
"""


def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] //= 2
            i += 1
        else:
            l.remove(l[i])


a = [1, 2, 3, 4, 5, 6]
b = [1, 3, 5]
modify_list(a)
print(a)
modify_list(b)
print(b)
