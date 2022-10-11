"""
Формат входных данных
На вход программе подается одно слово, записанное строчными русскими буквами без буквы "ё".

Формат выходных данных
Программа должна вывести в соответствии с указанным алгоритмом строки,
количество которых равно количеству разных букв в строке,
которая получается путем конкатенации введенного слова и строки "запретил букву".
"""

chars = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

line = input()
line += ' запретил букву '
i = 0
while len(line) > 0:
    if chars[i] not in line:
        i += 1
        continue
    line = line.lstrip().replace('  ', ' ') + chars[i]
    print(line)
    line = line.replace(chars[i], '')
    i += 1
    if line.isspace():
        break