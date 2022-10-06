"""
Напишите программу, которая меняет местами столбцы в матрице.
"""

import numpy as np


def get_dimensions():
    n = int(input())
    m = int(input())
    return n, m


def create_matrix():
    n, m = get_dimensions()
    matrix = np.zeros((n, m), dtype=np.int_)
    for i in range(n):
        matrix[i] = [int(el) for el in input().split()]
    return matrix


def print_matrix(matrix: np.array):
    n = matrix.shape[0]
    m = matrix.shape[1]
    for i in range(n):
        for j in range(m):
            print(str(matrix[i, j]).ljust(3), end='')
        print()


def change_columns_of_matrix(matrix: np.array):
    j1, j2 = (int(el) for el in input().split())
    n = matrix.shape[0]
    m = matrix.shape[1]
    for i in range(n):
        matrix[i, j1], matrix[i, j2] = matrix[i, j2], matrix[i, j1]
    return matrix


def main():
    matrix = create_matrix()
    print_matrix(change_columns_of_matrix(matrix))


if __name__ == '__main__':
    main()
