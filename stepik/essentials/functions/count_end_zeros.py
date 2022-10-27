# В этой задаче вам необходимо воспользоваться уже готовой функцией factorial,
# которая принимает неотрицательное число, и возвращает значение факториала данного числа.
#
# Ваша задача создать функцию trailing_zeros, которая принимает неотрицательное число,
# находит его факториал и возвращает сколько нулей на конце этого факториала .

def factorial(n: int):
    fc = 1
    for i in range(1, n + 1):
        fc *= i
    return fc


def trailing_zeros(n: int) -> int:
    fc = str(factorial(n))
    return len(fc) - len(fc.rstrip('0'))


for i in range(15):
    print(trailing_zeros(i))

print(trailing_zeros(20))