from functools import partial
import operator as op

x = int('1101', base=2)
print(f'x = {x}')

int_2 = partial(int, base=2)
y = int_2('1101')
print(f'y = {y}')

names = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(names)
sort_by_last(names)
print(names)

my_list = ['abs', 'abc', 'bda']
print(my_list)
sort_by_last(my_list)
print(my_list)
