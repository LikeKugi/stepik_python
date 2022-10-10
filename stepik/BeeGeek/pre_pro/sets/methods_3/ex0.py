# Подмножества
set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}

print(set1.issubset(set2))

set1 = {2, 3}
set2 = {1, 2, 3, 4, 5, 6}

print(set1 <= set2)

# Надмножества

set1 = {'a', 'b', 'c', 'd', 'e'}
set2 = {'c', 'e'}

print(set1.issuperset(set2))

set1 = {'a', 'b', 'c', 'd', 'e'}
set2 = {'c', 'e'}

print(set1 >= set2)

# Определение отсутствия общих элементов

set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7}
set3 = {7, 8, 9}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))
print(set2.isdisjoint(set3))