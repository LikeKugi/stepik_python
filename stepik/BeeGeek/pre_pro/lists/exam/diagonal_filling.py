"""
На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 0;
на двух диагоналях, прилегающих к главной, число 1;
на следующих двух диагоналях число 2, и т.д.
"""
import numpy as np

n = int(input())
matrix = np.zeros((n, n), dtype=np.int_)
for i in range(n):
    for j in range(n):
        if i != j:
            matrix[i,j] = abs(i-j)

for i in range(n):
    for j in range(n):
        print(str(matrix[i,j]).ljust(3),end='')
    print()