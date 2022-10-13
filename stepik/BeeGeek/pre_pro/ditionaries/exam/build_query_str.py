"""
Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса,
сформированную из этих параметров.

Примечание 1. В итоговой строке параметры должны быть отсортированы в лексикографическом порядке ключей словаря.
'='.join([key for key in sorted(params)]
"""

def build_query_string(params:dict):
    print(sorted(params))
    output = '&'.join([key+'='+str(params.get(key)) for key in sorted(params)])
    print(output)


print(build_query_string({'name': 'timur', 'age': 28}))
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))