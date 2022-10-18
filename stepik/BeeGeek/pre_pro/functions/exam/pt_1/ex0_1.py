def func(x=2, y=3):
    return x * y

print(func())

def func(x=2, y=3):
    return x * y

print(func(1))

def display(*args):
    for i in args:
        print(i, end=' ')

#display(name='Emma', age=25)

def display(**kwargs):
    for i in kwargs:
        print(i, end=' ')

display(emp='Kelly', salary=9000)

def outer_func(a, b):
    def inner_func(c, d):
        return c + d + a*b
    return inner_func

res = outer_func(5, 10)(3, 2)

print(res)

num = int('1000001')
print(num)

num = int('1000001', 2)
print(num)