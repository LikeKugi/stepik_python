"""
Сриниваса Рамануджан – индийский математик, славившийся своей интуицией в области чисел.
Когда английский математик Годфри Харди навестил его однажды в больнице, он обмолвился, что номером такси,
на котором он приехал, было 1729, такое скучное и заурядное число.
На что Рамануджан ответил: "Нет, нет! Это очень интересное число.
Это наименьшее число, выражаемое как сумма двух кубов двумя разными способами". Другими словами:
1729 = 1^3 + 12^3 = 9^3 + 10^3.

Напишите программу, которая находит аналогичные интересные числа.
В ответе запишите первые 5 чисел в порядке возрастания, включая число 1729.
"""

import taichi as ti

ti.init()


@ti.func
def cubes(number):
    flag = False
    max_index = 100
    for i in range(2, max_index):
        ci = i ** 3
        if flag:
            break
        for j in range(i, max_index):
            cj = j ** 3
            if flag:
                break
            if ci + cj == number:
                for k in range(i + 1, max_index):
                    ck = k ** 3
                    if flag:
                        break
                    for l in range(k, max_index):
                        cl = l ** 3
                        if flag:
                            break
                        if cl + ck == number:
                            print(i, j, k, l)
                            print(number)
                            flag = True


@ti.kernel
def print_number():
    for i in range(1730, 50000):
        cubes(i)


print_number()
