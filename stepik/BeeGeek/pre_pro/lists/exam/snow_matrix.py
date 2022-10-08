"""
На вход программе подается нечетное натуральное число n.
Напишите программу, которая создает матрицу размером n×n заполнив её символами '.'
Затем заполните символами '*' среднюю строку и столбец матрицы, главную и побочную диагональ матрицы.
Выведите полученную матрицу на экран, разделяя элементы пробелами.
"""
import numpy as np


def get_int_numbers(): return (int(el) for el in input().split())


def create_matrix(dims):
    matrix = np.zeros((dims, dims), dtype=np.int_)
    for i in range(dims):
        for j in range(dims):
            if (i == j) or (i == dims - j - 1) or (j == dims // 2) or (i == dims // 2):
                matrix[i, j] = 1
    return matrix


def print_matrix(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            print('.' if matrix[i, j] == 0 else '*', end=' ')
        print()


def main():
    count_rows = int(input())
    m1 = create_matrix(count_rows)
    print_matrix(m1)


if __name__ == '__main__':
    main()
