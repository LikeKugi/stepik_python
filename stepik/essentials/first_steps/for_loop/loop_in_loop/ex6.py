# put your python code here
n, m = map(int, input().split())
matrix = [[0 if el == '.' else 1 for el in input()] for _ in range(n)]
rows = 0
columns = 0
print(*matrix,sep='\n')
for i in range(n):
    if sum(matrix[i]) == 0:
        rows += 1
for j in range(m):
    if sum([matrix[i][j] for i in range(n)]) == 0:
        columns += 1
print(rows,columns)
print(rows * m + columns * (n - rows))
