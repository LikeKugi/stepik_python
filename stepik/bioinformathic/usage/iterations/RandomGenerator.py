from random import random


class RandomIterator:

    def __init__(self, k=5):
        self.__k = k
        self.__i = 0

    def __next__(self):
        if self.__i < self.__k:
            self.__i += 1
            return random()
        else:
            raise StopIteration

    def __iter__(self):
        return self


def random_generator(k):
    for i in range(k):
        yield random()

gen = random_generator(5)
print(type(gen))

for i in gen:
    print(i)