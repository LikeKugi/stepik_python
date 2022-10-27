# Ваша задача написать функцию format_name_list, которая принимает список словарей,
# у каждого словаря в этом списке есть только ключ name.
#
# Функция format_name_list должна вернуть строку, в которой все имена из списка разделяются запятой
# кроме последних двух имен, они должны быть разделены союзом "и". Если в списке нет ни одного имени,
# функция должна вернуть пустую строку.

def format_name_list(names: list[dict]) -> str:
    out_line = ''
    print(len(names))
    if names:
        out_line = ', '.join([names[i].get('name') for i in range(len(names) - 1)]) + (
        (f' and {names[-1]["name"]}', f'{names[-1]["name"]}')[len(names) < 2])
    return out_line


for x in [[{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}], [{'name': 'Bart'}, {'name': 'Lisa'}],
          [{'name': 'Bart'}], [], [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]]:
    print(format_name_list(x))
