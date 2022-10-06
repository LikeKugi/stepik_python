"""
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.
"""
import numpy as np


def get_dimension(): return int(input())


def create_matrix(n: int):
    matrix = np.zeros((n, n), dtype=np.int_)
    for i in range(n):
        matrix[i] = [int(el) for el in input().split()]
    return matrix


def check_for_symmetry(matrix: np.array, n: int):
    """
    Check for symmetry
    :param matrix:
    :param n:
    :return:
    >>> check_for_symmetry(np.array([[0,1,2],[1,2,3],[2,3,4]]),3)
    True
    >>> check_for_symmetry(np.array([[1,2],[2,4]]),2)
    True
    >>> check_for_symmetry(np.array([[5,3,7,1,5],[3,5,4,5,8],[5,4,4,8,4],[1,5,8,5,1],[5,7,4,1,5]]),5)
    False
    >>> check_for_symmetry(np.array([[5,3,7,1],[3,5,4,5],[7,4,4,8],[1,5,8,5]]),4)
    True
    """
    for i in range(n):
        for j in range(i):
            if matrix[i, j] != matrix[j, i]:
                return False
    return True


def main():
    n = get_dimension()
    matrix = create_matrix(n)
    if check_for_symmetry(matrix, n):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
    main()
