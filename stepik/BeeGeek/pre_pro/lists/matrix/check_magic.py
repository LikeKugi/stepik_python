"""
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
"""
import numpy as np


def get_dimension(): return int(input())


def create_matrix(n: int):
    return np.array([[int(el) for el in input().split()] for _ in range(n)], dtype=np.int_)


def check_magic(matrix: np.array):
    sum_magic = sum(matrix[0])
    n = matrix.shape[0]
    for i in range(1, n ** 2 + 1):
        if i not in matrix:
            return False
    for i in range(n):
        col = matrix[:, i]
        row = matrix[i]
        if sum(row) != sum_magic or sum(col) != sum_magic:
            return False
    sum_mdiag = sum(np.diag(matrix))
    sum_bdiag = sum(np.diag(np.flip(matrix, axis=1)))
    if sum_mdiag != sum_magic or sum_bdiag != sum_magic:
        return False
    return True


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
    if check_magic(matrix):
        print('YES')
    else:
        print('NO')
    print_matrix(matrix)


if __name__ == '__main__':
    main()
