import concurrent.futures
import threading
import time


class BankAccount:

    def __init__(self):
        self.balance = 100  # shared resource
        self.lock_obj = threading.Lock()

    def update(self, transaction, amount):
        print(f'{transaction} started')

        with self.lock_obj:
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount

        print(f'{transaction} ended')


def race_with_threadings():
    acc = BankAccount()
    print(f'Race with mistake started acc balance = {acc.balance}')

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as exx:
        exx.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f'Ended of Race with mistake, acc balance = {acc.balance}')


def race_with_lock():
    lock_obj = threading.Lock()
    print(lock_obj.locked())

    lock_obj.acquire()
    print(lock_obj.locked())

    lock_obj.release()
    print(lock_obj.locked())


if __name__ == '__main__':
    race_with_threadings()
