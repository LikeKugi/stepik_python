set1 = {10, 20, 30, 40}
set2 = {50, 20, '10', 60}

set3 = set1.union(set2)

print(len(set3))

set1 = {'Yellow', 'Orange', 'Black'}
set2 = {'Orange', 'Blue', 'Pink'}

set3 = set2.difference(set1)
print(set3)

set1 = {'Yellow', 'Orange', 'Black'}
set2 = {'Orange', 'Blue', 'Pink'}

set1.difference_update(set2)
print(set1)

myset = {'Yellow', 'Orange', 'Black'}

myset.update(['Blue', 'Green', 'Red', 'Orange'])
print(myset)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}

print(set1.issubset(set2))
print(set2.issuperset(set1))

myset = {'Yellow', 'Orange', 'Black'}
myset.discard('Blue')

print(myset)