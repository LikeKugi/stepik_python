class EvenLengthMixin:
    def is_even_length(self):
        return not len(self) % 2


class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, 12, 4, 17])
ml.sort()
print(ml)
ml.append(15)
print(ml.is_even_length())