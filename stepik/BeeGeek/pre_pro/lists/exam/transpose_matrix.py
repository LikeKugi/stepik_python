"""
Напишите программу, которая транспонирует квадратную матрицу.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы.

Формат выходных данных
Программа должна вывести транспонированную матрицу.
"""

import numpy as np


def get_int_numbers(): return (int(el) for el in input().split())


def create_matrix(row):
    matrix = np.array([[*get_int_numbers()] for _ in range(row)], dtype=np.int_)
    return matrix


def transpose_matrix(m1: np.array):
    return m1.T


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    row = int(input())
    m1 = create_matrix(row)
    m2 = transpose_matrix(m1)
    print_matrix(m2)


if __name__ == '__main__':
    main()