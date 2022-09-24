s = 0
k = 30
d = k - 5
k = 2 * d
s = k - 100

x = 3
y = 4
z = x + y
z = z + 1
x = y
y = 5
x = z + y + 7

number = int(input())
for i in range(3):
    print(number + i)

a = int(input())
print('Объем =', a ** 3)
print('Площадь полной поверхности =', 6 * (a ** 2))

a, b = int(input()), int(input())
print(3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41)
