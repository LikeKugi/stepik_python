#  Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой

n, m = map(int, input().split())
el = 0
numbers = []
for i in range(n):
    numbers.append([])
    for j in range(m):
        numbers[i].append(el)
        el+=1
    if i%2:
        numbers[i].reverse()




for i in range(n):
    for j in range(m):
        print(numbers[i][j], end=' ')
    print()
