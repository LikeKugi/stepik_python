from random import uniform as ru
import time

n = 10 ** 7    # количество испытаний
k = 0           # количество точек внутри фигуры
s0 = 4         # площадь квадрата в котором фигура

time_start = time.time()
for _ in range(n):
    x = ru(-1, 1)
    y = ru(-1, 1)

    if x**2 + y**2 <=1:
        k+=1
time_end = time.time()

print(time_end - time_start)

print((k/n)*s0)