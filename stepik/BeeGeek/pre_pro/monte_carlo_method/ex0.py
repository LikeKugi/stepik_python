"""

0≤x≤1
0≤y≤1
y≤x**2

"""

import random

n = 1000
k = 0
s0 = 1
for _ in range(n):
    x = random.uniform(0, 1)  # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(0, 1)  # случайное число с плавающей точкой от 0 до 1

    if y <= x ** 2:  # если попадает в нужную область
        k += 1

print((k / n) * s0)
