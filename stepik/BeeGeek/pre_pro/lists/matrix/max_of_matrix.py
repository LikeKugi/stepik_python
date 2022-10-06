"""
На вход программе подаются два натуральных числа n и m — количество строк и столбцов в матрице,
затем n строк по m целых чисел в каждой, отделенных символом пробела.

Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.

Формат входных данных
На вход программе на разных строках подаются два числа n и m — количество строк и столбцов в матрице,
затем сами элементы матрицы построчно через пробел.

Формат выходных данных
Программа должна вывести два числа: номер строки и номер столбца, в которых стоит наибольший элемент таблицы.
Если таких элементов несколько, то выводится тот, у которого меньше номер строки,
а если номера строк равны то тот, у которого меньше номер столбца.

Примечание. Считайте, что нумерация строк и столбцов начинается с нуля.
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


def find_max_of_matrix(matrix: np.array):
    max_i, max_j = 0, 0
    n = matrix.shape[0]
    m = matrix.shape[1]
    for i in range(n):
        for j in range(m):
            if matrix[i, j] > matrix[max_i, max_j]:
                max_i, max_j = i, j
    return max_i, max_j


def main():
    matrix = create_matrix()
    print_matrix(matrix)
    print(*find_max_of_matrix(matrix))


if __name__ == '__main__':
    main()
