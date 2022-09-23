d = {'a': 239, 10: 100}
print(d['a'])
print(d[10])

print(dict)

dictionary = {1: 10, 'ds': 15, 2: 'hs'}
print(2 in dictionary)
print('a' not in dictionary)
print(dictionary[2])
dictionary['ls'] = 'you'
print(dictionary['ls'])
print(dictionary.get(2))
print(dictionary.get('rs'))
del dictionary['ds']
print(dictionary)

d = {'c': 14, 'a': 12, 't': 9, 'g': 18}
for key in d:
    print(key, end=' ')
print()

for key in d.keys():
    print(key, end=' ')
print()

for value in d.values():
    print(value, end=' ')
print()

for key, value in d.items():
    print(key, ':', value,  end="; ")
print()
