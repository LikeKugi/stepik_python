a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


def gcd_minus(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(f'Нод={a}')


def gcd_divide(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    print(f'Нод={a}')


gcd_minus(a, b)
gcd_divide(a, b)
