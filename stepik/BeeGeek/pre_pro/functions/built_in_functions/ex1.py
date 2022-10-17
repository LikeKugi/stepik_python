from operator import mul
from functools import reduce

result = reduce(mul, range(1, 6))
print(result)

from operator import add

result = list(map(add, 'abc', '1234'))
print(result)

result = list(map(mul, ['a', 'b', 'c'], [1, 2, 3]))
print(result)

result = reduce(add, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(result)