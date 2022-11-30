import threading
import time
from count_threesome import read_ints, count_three_sum

if __name__ == '__main__':
    print('started main')
    ints = read_ints('2Kints.txt')

    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    start = time.perf_counter()
    t1.start()
    t1.join()
    end = time.perf_counter()

    print(f'time done: {end - start}')
