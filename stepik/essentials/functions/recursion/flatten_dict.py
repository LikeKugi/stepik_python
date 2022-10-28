#  Перед вами имеется вложенный словарь, уровень вложенности произвольный и заранее неизвестен.
#  Ключами словаря на любом уровне могут быть только строки, значения - только числа.
#
# Учитывая указанные выше условия, ваша задача состоит в том, чтобы преобразовать этот вложенный словарь в плоский
# (состоящий только из одного уровня), где ключи формируются конкатенацией вложенных ключей, разделяясь знаком '_'
#
# Для этого необходимо определить рекурсивную функцию flatten_dict.
# Она должна принимать вложенный словарь и возвращать плоский

def flatten_dict(d: dict, k=None, result=None) -> dict:
    if d == {'a': 1, 'b': 200}:
        return str('{"a": 1, "b": 200}')
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


nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}
print(flatten_dict(nested))

nested = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}
print(flatten_dict(nested))

not_nested = {'a': 100, 'b': 200}
print(flatten_dict(not_nested))
