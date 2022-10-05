"""
На вход программе подаются два натуральных числа n и m, каждое на отдельной строке —
количество строк и столбцов в матрице. Далее вводятся сами элементы матрицы — слова,
каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.
"""

n, m = int(input()), int(input())
words = [input() for _ in range(n * m)]
matrix = list()
k = 0
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[-1].append(words[k])
        k += 1
for row in matrix:
    print(' '.join(row))
print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()
