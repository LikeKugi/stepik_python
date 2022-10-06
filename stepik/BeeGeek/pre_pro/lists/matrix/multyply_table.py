"""
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице.
Создайте матрицу mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.

Формат входных данных
На вход программе на разных строках подаются два числа nn и mm — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести таблицу умножения отводя на вывод каждого числа ровно 3 символа
(для этого используйте строковый метод ljust()).
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
        for j in range(m):
            matrix[i, j] = i * j
    return matrix


def print_matrix(matrix: np.array):
    n = matrix.shape[0]
    m = matrix.shape[1]
    for i in range(n):
        for j in range(m):
            print(str(matrix[i, j]).ljust(3), end='')
        print()


def main():
    matrix = create_matrix()
    print_matrix(matrix)


if __name__ == '__main__':
    main()
