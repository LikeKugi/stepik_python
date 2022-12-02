from functools import lru_cache, wraps
import math
import time


def time_func(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(func.__doc__)
        start = time.perf_counter()
        out = func(*args, **kwargs)
        print(f'Time needed: {time.perf_counter() - start}')
        return out

    return inner


@lru_cache(None)
def find_gcd_recursive(a: int, b: int) -> int:
    """recursive"""
    if not a or not b:
        return a or b
    if a >= b:
        return find_gcd_recursive(a % b, b)
    else:
        return find_gcd_recursive(a, b % a)


@time_func
def start_recursive(*args, **kwargs):
    """recursive start"""
    out = find_gcd_recursive(*args, **kwargs)
    return out


@time_func
def find_gcd_for_loop(a: int, b: int) -> int:
    """for loop"""
    counter = math.ceil(2 * math.log2(max(a, b)))
    for _ in range(counter):
        a, b = max(a, b), min(a, b)
        mod = a % b
        if mod == 0:
            return min(a, b)
        else:
            a = mod


@time_func
def find_gcd_while_loop(a: int, b: int) -> int:
    """while loop"""
    a, b = max(a, b), min(a, b)
    while a and b:
        a, b = b, a % b
    else:
        return a


if __name__ == '__main__':
    print(start_recursive(3918848, 1653264))
    print('/----------------------------------/')
    print(find_gcd_for_loop(3918848, 1653264))
    print('/----------------------------------/')
    print(find_gcd_while_loop(3918848, 1653264))
    print('/----------------------------------/')
    print(find_gcd_while_loop(14159572, 63967072))
    print('/----------------------------------/')
    print(find_gcd_while_loop(154141321654131451541344623, 125435854378654))
    print('/----------------------------------/')
