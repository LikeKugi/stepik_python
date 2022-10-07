"""
На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n×n заполнив её в соответствии с образцом.

Формат входных данных
На вход программе подается натуральное число n — количество строк и столбцов в матрице.

Формат выходных данных
Программа должна вывести указанную матрицу в соответствии с образцом:
разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.
"""

n = int(input())
matrix = [[0] * n for _ in range(n)]


def x_cross(matrix: list):
    for i in range(n):
        for j in range(n):
            if i == j or i == n - j - 1:
                matrix[i][j] = 1
            print(str(matrix[i][j]).ljust(3), end='')
        print()


def clocks_cross(matrix: list):
    for i in range(n):
        for j in range(n):
            if (i <= j and i <= n-1-j) or (i >=j and i >= n-j-1):
                matrix[i][j] = 1
            print(str(matrix[i][j]).ljust(3), end='')
        print()

clocks_cross(matrix)