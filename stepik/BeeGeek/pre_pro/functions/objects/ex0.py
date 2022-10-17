s1 = 'python'
s2 = 'stepicon'
s3 = 'beegeek'

print(min(s1, s2, s3))
print(max(s1, s2, s3))

print(min(s1, s2, s3, key=len))
print(max(s1, s2, s3, key=len))


def f(x):
    return x ** 2


g = f
print(f(3), g(5))


def f(x):
    return x**2


def g(x):
    return x**3


funcs = [f, g]
print(funcs[0](5), funcs[1](5))


def comparator(pair):
    return pair[1]


pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
pairs.sort(key=comparator)
print(pairs)

def comparator(pair):
    return pair[0] + pair[1]

pairs.sort(key=comparator, reverse=True)
print(pairs)

words = ['this', 'is', 'a', 'test', 'of', 'sorting']
words.sort(key=len)
print(words)


def f1(x):
    return 2*x+1


def f2(x):
    return x**2


def f3(x):
    return -x**2+1


def f4(x):
    return x-3


funcs = [f1, f2, f3, f4]
i = int(input())
print(funcs[i](2))