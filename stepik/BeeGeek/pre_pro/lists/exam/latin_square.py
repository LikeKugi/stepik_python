"""
Латинским квадратом порядка n называется квадратная матрица размером n×n,
каждая строка и каждый столбец которой содержат все числа от 1 до n.
Напишите программу, которая проверяет, является ли заданная квадратная матрица латинским квадратом.
"""
import numpy as np


def get_int_numbers(): return (int(el) for el in input().split())


def create_matrix(row):
    matrix = np.array([[*get_int_numbers()] for _ in range(row)], dtype=np.int_)
    return matrix


def is_latin(matrix: np.array, n):
    numbers = [el for el in range(1,n+1)]
    for number in numbers:
        for i in range(n):
            if number not in matrix[:,i] or number not in matrix[i,:]:
                return False
    return True


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    row = int(input())
    m1 = create_matrix(row)
    if is_latin(m1, row):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()