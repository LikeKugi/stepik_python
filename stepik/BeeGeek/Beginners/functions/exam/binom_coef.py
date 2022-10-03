"""
Напишите функцию compute_binom(n, k),
которая принимает в качестве аргументов два натуральных числа n и k и возвращает значение биномиального коэффициента,
равного n! / (k! * (n-k)!)

"""

from math import factorial as fc


def compute_binom(n, k):
    return fc(n) / (fc(k) * fc(n - k))

print(compute_binom(1, 1))
print(compute_binom(2, 1))
print(compute_binom(10, 1))
print(compute_binom(15, 2))