"""
Дана квадратная матрица чисел.
Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали,
при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами
элемент на главной диагонали и на побочной диагонали).
"""
import numpy as np


def get_dimension(): return int(input())


def create_matrix(n: int):
    return np.array([[int(el) for el in input().split()] for _ in range(n)], dtype=np.int_)


def change_diagonals(matrix: np.array):
    n = matrix.shape[0]
    for i in range(n):
        matrix[i, i], matrix[n - i - 1, i] = matrix[n - i - 1, i], matrix[i, i]


def print_matrix(matrix: np.array):
    n = matrix.shape[0]
    m = matrix.shape[1]
    for i in range(n):
        for j in range(m):
            print(matrix[i, j], end=' ')
        print()


def main():
    dimension = get_dimension()
    matrix = create_matrix(dimension)
    change_diagonals(matrix)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
