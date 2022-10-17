from functools import reduce

numbers = range(10)
obj = map(lambda x: x + 1, numbers)
obj = filter(lambda x: x % 2 == 1, obj)
result = reduce(lambda x, y: x + y, obj, 0)

print(result)

result = list(map(lambda x: x.split(), ['a', 'a b', 'a b c']))

print(result)

high_ord_func = lambda x, func: x + func(x)

result = high_ord_func(2, lambda x: x * x) + high_ord_func(5, lambda x: x + 3)

print(result)

dict1 = {'x': 1}
dict2 = {'y': 2}
dict3 = {'x': 3, 'y': 4}

result = list(filter(lambda d: 'x' in d.keys(), [dict1, dict2, dict3]))

print(result)