#  Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания,
#  начиная с числа 2.

def is_prime(n):
    if n in {2,3}:
        return True
    if not (n%2 and n%3):
        return False
    for i in range(1, int(n**0.5)):
        if not n%(6*i-1) and (6*i-1) < n:
            return False
        if not n%(6*i+1) and (6*i+1) < n:
            return False