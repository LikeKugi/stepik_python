#  Дано натуральное число N. Определить, является ли оно простым.
#  Натуральное число N называется простым, если у него есть только два делителя: единица и само число N.

n = int(input())


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False
    for i in range(1, n):
        if (6 * i - 1) > n:
            return True
        if n % (6 * i - 1) == 0 and (6 * i - 1) != n:
            return False
        if n % (6 * i + 1) == 0 and (6 * i + 1) != n:
            return False
    return True


print(('No', 'Yes')[is_prime(n)])

for i in range(20):
    print(i, is_prime(i))