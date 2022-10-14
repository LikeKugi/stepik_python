from random import uniform as ru

n = 10 ** 6     # количество испытаний
k = 0           # количество точек внутри фигуры
s0 = 16         # площадь квадрата в котором фигура

for _ in range(n):
    x = ru(-2, 2)
    y = ru(-2, 2)

    if x**3 + y**4 + 2 >=0 and 3*x + y**2 <=2:
        k+=1

print((k/n)*s0)
