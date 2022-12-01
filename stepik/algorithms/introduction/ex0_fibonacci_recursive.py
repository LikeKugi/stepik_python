from functools import lru_cache, singledispatch
from typing import Literal


@singledispatch
@lru_cache(maxsize=1024)
def fibonacci(n: int, *, recursive=Literal[True]) -> int:
    """
    find recursive number of Fibonacci
    :param recursive: bool
        True if need recursive
        False if dynamic
    :param n: int
        number to find
    :return: int
        the value of Fibonacci for n
    """
    if n in {0, 1}:
        return n
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)


@fibonacci.register
def _(n: int, *, recursive=Literal[False]) -> int:
    fib_array = [0, 1]
    for i in range(n-1):
        fib_array.append(fib_array[-1] + fib_array[-2])
    return fib_array[-1]


if __name__ == '__main__':
    print(fibonacci(200, recursive=True))
