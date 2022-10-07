"""
На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m заполнив её "диагоналями" в соответствии с образцом.

Формат входных данных
На вход программе на одной строке подаются два натуральных числа n и m — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом.
"""
import numpy as np

n, m = (int(el) for el in input().split())
matrix = np.zeros((n, m), dtype=np.int_)
tp = 1
for el in range(n + m):
    for i in range(n):
        for j in range(m):
            if i + j == el:
                matrix[i, j] = tp
                tp += 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i,j]).ljust(3),end='')
    print()
