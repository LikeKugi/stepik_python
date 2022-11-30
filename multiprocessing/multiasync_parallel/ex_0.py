import time
from count_threesome import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')
    start = time.perf_counter()
    ints = read_ints('2Kints.txt')
    count_three_sum(ints)
    end = time.perf_counter()
    print(f'time done: {end - start}')
