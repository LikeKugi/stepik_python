from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda x, y: x + y, numbers)
print(result)

numbers = [1, 2, 3]
result = reduce(lambda a, b: a * b, numbers, 10)
print(result)

words = ['beegeek', 'stepik', 'python', 'iq-option']
result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(result)

result = reduce(lambda s, x: s + str(x), [1, 2, 3, 4, 5], '+')
print(result)


import operator

def flatten(data):
    return reduce(operator.concat, data, [])

result = flatten([[1, 2], [3, 4], [], [5]])

print(result)