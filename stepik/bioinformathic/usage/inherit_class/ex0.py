class MyList(list):
    def is_even_length(self):
        return not len(self) % 2


x = MyList()
print(x)
print(isinstance(x,list))
x.extend([1, 2, 3, 4, 5])
print(x.is_even_length())
x.append(6)
print(x)
print(x.is_even_length())