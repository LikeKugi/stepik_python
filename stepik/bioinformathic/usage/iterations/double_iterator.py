class DoubleElementListIterator:
    def __init__(self, lst):
        self.__lst = lst
        self.__i = 0

    def __next__(self):
        if self.__i < len(self.__lst):
            self.__i += 2
            return self.__lst[self.__i - 2], self.__lst[self.__i - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


for pair in MyList([1, 2, 3, 4, 5, 6]):
    print(pair)
