from random import random


class RandomIterator:

    def __init__(self, k):
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


x = RandomIterator(10)

for i in x:
    print(i)

