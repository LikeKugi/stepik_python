number = int(input())
print('Следующее за числом', number, 'число:', number + 1)
print('Для числа', number, 'предыдущее число:', number - 1)

print(int(input()) + int(input()) + int(input()) + int(input()))

n1, n2 = int(input()), int(input())
print(n1, '+', n2, '=', n1 + n2)
print(n1, '-', n2, '=', n1 - n2)
print(n1, '*', n2, '=', n1 * n2)

a, d, n = int(input()), int(input()), int(input())
print(a + d * (n - 1))

number = int(input())
for i in range(5):
    print(number * i, end='---')
