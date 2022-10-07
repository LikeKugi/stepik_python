import numpy as np

n, m = (int(el) for el in input().split())
matrix = np.zeros((n, m), dtype=np.int_)
for i in range(n):
    for j in range(m):
        matrix[i, j] = (i + j) % m + 1

for i in range(n):
    for j in range(m):
        print(str(matrix[i,j]).ljust(3),end='')
    print()
