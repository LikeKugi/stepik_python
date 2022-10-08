"""
Напишите программу для вычисления суммы двух матриц.

Формат входных данных
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрицах,
затем элементы первой матрицы, затем пустая строка, далее следуют элементы второй матрицы.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""
import numpy as np


def get_int_numbers(): return (int(el) for el in input().split())


def create_matrix(row, column):
    matrix = np.array([[*get_int_numbers()] for _ in range(row)], dtype=np.int_)
    return matrix


def sum_matrix(m1: np.array, m2: np.array):
    return m1 + m2


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    row, column = get_int_numbers()
    m1 = create_matrix(row, column)
    m2 = create_matrix(row, column)
    m3 = sum_matrix(m1, m2)
    print_matrix(m3)


if __name__ == '__main__':
    main()


