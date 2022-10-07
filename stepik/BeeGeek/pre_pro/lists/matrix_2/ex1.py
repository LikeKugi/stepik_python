"""
На вход программе подаются два натуральных числа n и m.
Напишите программу для создания матрицы размером n×m, заполнив её символами . и * в шахматном порядке.
В левом верхнем углу должна стоять точка. Выведите полученную матрицу на экран, разделяя элементы пробелами.
"""

samples = {0: '.', 1: '*'}


def get_dimensions(): return (int(el) for el in input().split())


def create_matrix(row, column):
    matrix = [[samples.get((i + j) % 2) for j in range(column)] for i in range(row)]
    return matrix


def print_matrix(matrix: list):
    for row in matrix:
        print(*row)


def main():
    n, m = get_dimensions()
    matrix = create_matrix(n, m)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
