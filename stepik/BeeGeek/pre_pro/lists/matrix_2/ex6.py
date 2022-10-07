"""
На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m заполнив её "змейкой" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.
"""
import numpy as np

n, m = (int(el) for el in input().split())
arr = np.arange(1, (n * m + 1), 1, dtype=np.int_)
matrix = arr.reshape(n, m)
for i in range(n):
    if i % 2 != 0:
        matrix[i] = matrix[i][::-1]
for i in range(n):
    for j in range(m):
        print(str(matrix[i, j]).ljust(3), end='')
    print()
