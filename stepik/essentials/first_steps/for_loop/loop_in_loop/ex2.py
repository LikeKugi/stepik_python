"""
Задана система уравнений:
a^2 + b = n
a + b^2 = m
Нужно посчитать количество пар целых чисел (a,b) (0 ≤ a , b ), которые удовлетворяют системе.
"""

n, m = map(int, input().split())
counter = 0
for i in range(n):
    for j in range(m):
        if (i**2 + j == n) and (i + j**2 == m):
            counter += 1
print(counter)


