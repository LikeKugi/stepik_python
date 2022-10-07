"""
На вход программе подаются два натуральных числа n и m.
Напишите программу, которая создает матрицу размером n×m
и заполняет её числами от 1 до n*m.
"""
import numpy as np


def get_dimensions(): return (int(el) for el in input().split())


def print_matrix(matrix: np.array, rows, column):
    matrix = matrix.reshape(rows, column)
    for col in range(column):
        for row in range(rows):
            print(str(matrix[row, col]).ljust(3), end='')
        print()


n, m = get_dimensions()
matrix = np.arange(1, (n * m + 1), 1, dtype=int)
print_matrix(matrix, rows=m, column=n)

