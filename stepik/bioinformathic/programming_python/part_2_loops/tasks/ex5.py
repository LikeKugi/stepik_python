"""
Выведите таблицу размером n * n, заполненную числами от 1 до n^2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке
"""

n = int(input())

numbers = []
for i in range(n):
    numbers.append([])
    for j in range(n):
        numbers[i].append(0)

direction = 0
i=0
j=0
for el in range(1,n**2+1):
    numbers[i][j] = el
    direction%=4
    if direction == 0:
        if j < n-1 and numbers[i][j+1] == 0:
            j+=1
        else:
            direction +=1
            i+=1
            continue
    elif direction == 1:
        if i < n-1 and numbers[i+1][j] == 0:
            i+=1
        else:
            direction +=1
            j -=1
            continue
    elif direction == 2:
        if j > 0 and numbers[i][j-1] ==0:
            j-=1
        else:
            direction +=1
            i-=1
            continue
    elif direction == 3:
        if i > 0 and numbers[i-1][j]==0:
            i-=1
        else:
            direction +=1
            j+=1
            continue
for i in range(n):
    for j in range(n):
        print(numbers[i][j],end=' ')
    print()