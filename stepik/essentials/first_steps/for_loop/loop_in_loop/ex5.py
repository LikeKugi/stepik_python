n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]
print(*field, sep='\n')
counter = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == '.':
            if field[i - (1, 0)[i == 0]][j] == field[i + (1, 0)[i == n - 1]][j] == field[i][j - (1, 0)[j == 0]] == field[i][j + (1, 0)[j == m - 1]] == '.':
                counter += 1
            print(i, j, field[i - (1, 0)[i == 0]][j])
            print('   ', field[i + (1, 0)[i == n - 1]][j])
            print('   ', field[i][j - (1, 0)[j == 0]])
            print('   ', field[i][j + (1, 0)[j == m - 1]])

print(counter)
