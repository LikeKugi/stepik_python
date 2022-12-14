"""
Напишите функцию merge(), объединяющую словари в один общий.
Функция должна принимать список словарей и возвращать словарь, каждый ключ которого содержит множество
(тип данных set) уникальных значений собранных из всех словарей переданного списка.
"""
def merge(values):      # values - это список словарей
    output = {}
    for value in values:
        for k,v in value.items():
            output.setdefault(k,set()).add(v)
    print(output)


result = merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}])