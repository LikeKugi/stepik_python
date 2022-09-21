"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк.
После последней строки матрицы идёт строка, содержащая только строку "end".

Программа должна вывести матрицу того же размера, у которой каждый элемент
в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
"""
matrix = []
while True:
    str = input()
    if str == 'end':
        break
    matrix.append([int(i) for i in str.split()])
output = matrix.copy()
r = len(matrix)
for i in range(r):
    output[i] = matrix[i].copy()
    c = len(matrix[i])
    for j in range(c):
        output[i][j]=0
        dpi = i+1 if i+1<r else 0
        dmi = i-1 if i-1>=0 else -1
        dpj = j+1 if j+1<c else 0
        dmj = j-1 if j-1>=0 else -1
        output[i][j] = matrix[dmi][j] + matrix[dpi][j] + matrix[i][dmj] + matrix[i][dpj]
print()
for i in range(r):
    for j in range(len(output[i])):
        print(output[i][j],end=' ')
    print()
print(matrix)
print(output)
