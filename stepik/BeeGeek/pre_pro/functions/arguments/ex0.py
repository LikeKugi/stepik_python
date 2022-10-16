def f(n=3):
    return n + 7


print(f(f(f())))

def func(x, y, *args):
    return len(args)


print(func(10, 20, 30, 40, 50, 60))

def func(*args):
    return max(args) + min(args)


print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))