"""
На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m заполнив её "спиралью" в соответствии с образцом.
"""
import numpy as np

n, m = (int(el) for el in input().split())

numbers = np.zeros((n, m), dtype=np.int_)

direction = 0
i = 0
j = 0
for el in range(1, n * m + 1):
    numbers[i, j] = el
    direction %= 4
    if direction == 0:
        if j < m - 1 and numbers[i, j + 1] == 0:
            j += 1
        else:
            direction += 1
            i += 1
            continue
    elif direction == 1:
        if i < n - 1 and numbers[i + 1, j] == 0:
            i += 1
        else:
            direction += 1
            j -= 1
            continue
    elif direction == 2:
        if j > 0 and numbers[i, j - 1] == 0:
            j -= 1
        else:
            direction += 1
            i -= 1
            continue
    elif direction == 3:
        if i > 0 and numbers[i - 1, j] == 0:
            i -= 1
        else:
            direction += 1
            j += 1
            continue
for i in range(n):
    for j in range(m):
        print(str(numbers[i, j]).ljust(3), end='')
    print()
