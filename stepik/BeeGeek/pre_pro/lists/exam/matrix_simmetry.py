"""
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.
"""

import numpy as np


def get_int_numbers(): return (int(el) for el in input().split())


def create_matrix(row):
    matrix = np.array([[*get_int_numbers()] for _ in range(row)], dtype=np.int_)
    return matrix


def check_simmetry(matrix: np.array, n):
    for i in range(n):
        for j in range(n):
            if matrix[i, j] != matrix[n - j - 1, n - i - 1]:
                return False
    return True


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    row = int(input())
    m1 = create_matrix(row)
    if check_simmetry(m1, row):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()