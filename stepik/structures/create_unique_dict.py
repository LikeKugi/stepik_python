# Программа на Python. Пусть имеется следующий словарь:
#
# d = {'one': 1, 'two': 2, 'natural': 1, 'True': 1, 'even': 2, 'three': 3, 'False': 0}
# Сформируйте из него другой словарь d_unique, состоящий из данных с уникальными значениями (оставлять нужно последнее
# значение, остальные отбрасывать).

d = {'one': 1, 'two': 2, 'natural': 1, 'True': 1, 'even': 2, 'three': 3, 'False': 0}

d_unique = {val: key for key, val in {v: k for k, v in d.items()}.items()}
print(d_unique)