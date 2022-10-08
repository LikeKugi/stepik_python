"""
Напишите программу, которая возводит квадратную матрицу в m-ую степень.

Формат входных данных
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы, затем натуральное число m.

Формат выходных данных
Программа должна вывести результирующую матрицу, разделяя элементы символом пробела.
"""
import numpy as np
from numpy.linalg import matrix_power as mp


def get_int_numbers(): return (int(el) for el in input().split())


def create_matrix(row, column):
    matrix = np.array([[*get_int_numbers()] for _ in range(row)], dtype=np.int_)
    return matrix


def pow_matrix(m1: np.array, pow: int):
    return mp(m1, pow)


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    row = column = int(input())
    m1 = create_matrix(row, column)
    power = int(input())
    m2 = pow_matrix(m1, power)
    print_matrix(m2)


if __name__ == '__main__':
    main()
