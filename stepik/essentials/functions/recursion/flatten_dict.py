#  Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен.
#  Ключами словаря на любом уровне могут быть только строки, значения - только числа.
#
# Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский
# (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, разделяясь знаком '_'
#
# Для этого необходимо определить рекурсивную функцию flatten_dict.
# Она должна принимать вложенный словарь и возвращать плоский

def flatten_dict(d: dict, k=None, result=None) -> dict:

    if result is None:
        result = {}
    for key in d.keys():

        if isinstance(d.get(key), dict):
            if k:
                k += '_' + key
            flatten_dict(d[key], k or key, result)
        else:
            result[(k + '_' + key) if k else key] = d.get(key)

    return result


def flatten_dict_(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}
print(flatten_dict(nested))

nested = {'a':1, 'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}
print(flatten_dict(nested))

nested = {'a': 1,
 'c': {'a': 2,
       'b': {'x': 5,
             'y' : 10}},
 'd': [1, 2, 3]}
print(flatten_dict(nested))

not_nested = {'a': 100, 'b': 200}
print(flatten_dict(not_nested))

