"""
На вход программе подается два натуральных числа a и b (a< b).
Напишите программу, которая находит все простые числа от a до b включительно.
"""
import math


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False
    else:
        for i in range(1, int(math.sqrt(n) + 1)):
            if (n % (6 * i - 1) == 0 and (6 * i - 1) < n) or (n % (6 * i + 1) == 0 and (6 * i + 1) < n):
                return False
    return True


a, b = int(input()), int(input())
for i in range(a, b + 1):
    if is_prime(i):
        print(i)
