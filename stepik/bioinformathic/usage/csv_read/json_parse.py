# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
# У каждого JSON-объекта есть поле name, которое содержит имя класса,
# и поле parents, которое содержит список имен прямых предков.
#
# Для каждого класса вычислите предком скольких классов он является

import json


def get_json():
    data = json.loads(input())
    return data


def get_children(data):
    children = {}

    for class_name in data:
        children.setdefault(class_name.get('name'), [])

        if class_name.get('parents'):
            for el in class_name.get('parents'):
                children.setdefault(el, []).append(class_name.get('name'))

    return children


def count_children(query, children):
    counter = set()
    for el in children.get(query):
        counter.add(el)
        counter.update(count_children(el, children))
    return counter


def print_dict(data):
    print(*[f'{key} : {len(value) + 1}' for key, value in sorted(data.items())], sep='\n')


def main():
    data = get_json()
    child_classes = get_children(data)
    print(child_classes)
    counts = {}
    for key in child_classes.keys():
        counts.setdefault(key, set()).update(count_children(key, child_classes))

    print_dict(counts)


if __name__ == '__main__':
    main()
