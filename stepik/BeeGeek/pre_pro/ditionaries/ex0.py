my_dict = dict([('first', 1), ('second', 2), ('third', 3)])

print(my_dict)

my_dict = dict.fromkeys(['a', 'b', 'c'], -1)

#print(my_dict['d'])

my_dict = {1: [0, 1], 2: [2, 3], 3: [4, 5]}

print(my_dict[2][1])

dict1 = {'key1':1, 'key2':2}
dict2 = {'key2':2, 'key1':1}

print(dict1 == dict2)

my_dict = {'foo': 100, 'bar': 200, 'baz': 300}

#print(my_dict['bar':'baz'])