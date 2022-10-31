class EvenLengthMixin:
    def is_even_len(self):
        return not len(self) % 2


class MyList(list, EvenLengthMixin):
    pass


print(MyList.mro())
x = MyList([1,2,3,4])
print(x.is_even_len())
x.append(6)
print(x.is_even_len())