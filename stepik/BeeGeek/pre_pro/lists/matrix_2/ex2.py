"""
На вход программе подается натуральное число n.
Напишите программу, которая создает матрицу размером n×n и заполняет её по следующему правилу:

числа на побочной диагонали равны 1;
числа, стоящие выше этой диагонали, равны 0;
числа, стоящие ниже этой диагонали, равны 2.
"""
import numpy as np

n = int(input())

arr = np.zeros((n, n), dtype=int)

for i in range(n):
    for j in range(n):
        if i == n - j - 1:
            arr[i, j] = 1
        elif i > n - j - 1:
            arr[i, j] = 2

for row in arr:
    print(*row)
