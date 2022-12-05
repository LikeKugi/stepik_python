import time
from functools import wraps


def measure_time(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        print(f'func executed in {elapsed:0.2f} seconds')
        return result

    return inner


def async_measure_time(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        elapsed = time.perf_counter() - start

        print(f'func executed in {elapsed:0.2f} seconds')
        return result

    return inner