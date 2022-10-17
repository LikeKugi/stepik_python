"""
Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера.
При этом (в зависимости от переданных аргументов) она должна вести себя так:

matrix() — возвращает матрицу 1× 1, в которой единственное число равно нулю;
matrix(n) — возвращает матрицу n× n, заполненную нулями;
matrix(n, m) — возвращает матрицу из n строк и m столбцов, заполненную нулями;
matrix(n, m, value) — возвращает матрицу из n строк и m столбцов, в которой каждый элемент равен числу value.
При создании функции пользуйтесь аргументами по умолчанию.
"""


def matrix(n=1, m=None, value=0):
    if not m:
        m = n
    matrix = [[value]*m for _ in range(n)]
    return list(matrix)


print(matrix())  # матрица 1 × 1 из 0
print(matrix(3))  # матрица 3 × 3 из 0
print(matrix(2, 5))  # матрица 2 × 5 из 0
print(matrix(3, 4, 9))  # матрица 3 × 4 из 9