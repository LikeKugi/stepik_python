class MyClass:
    a=10
    def func(self):
        print('hello')

a = MyClass()
print(a.a)

MyClass.func(a)


x = MyClass()
print(type(x))
print(type(MyClass))