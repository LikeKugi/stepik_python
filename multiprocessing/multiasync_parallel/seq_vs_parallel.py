import threading

from count_threesome import read_ints, count_three_sum
from decorators import measure_time


@measure_time
def run_in_parallel(numbers):
    t1 = threading.Thread(target=count_three_sum, daemon=True, kwargs={'ints': numbers, 'thread_name': 'Parallel-1'})
    t2 = threading.Thread(target=count_three_sum, daemon=True, kwargs={'ints': numbers, 'thread_name': 'Parallel-2'})

    t1.start()
    t2.start()

    print('running')

    t1.join()
    t2.join()


@measure_time
def run_sequentially(ints):
    count_three_sum(ints, 'main-1')


if __name__ == '__main__':
    print('started main')
    numbers = read_ints('1Kints.txt')

    run_in_parallel(numbers)
    numbers = read_ints('2Kints.txt')
    run_sequentially(numbers)
