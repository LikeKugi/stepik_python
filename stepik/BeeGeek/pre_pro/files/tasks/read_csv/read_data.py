"""
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.
Напишите функцию read_csv для чтения данных из этого файла. Она должна возвращать список словарей,
интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов.
"""


def read_csv():
    data = []
    with open('data.csv') as inf:
        titles = list(map(str.rstrip, inf.readline().split(',')))
        lines = list()
        for line in inf.readlines():
            lines.append(list(map(str.rstrip, line.split(','))))

    for i in range(len(lines)):
        data.append({})
        for j in range(len(titles)):
            data[-1][titles[j]] = lines[i][j]
    return data


read_csv()
