"""
На вход программе подается строка текста.
Если в этой строке буква «f» встречается только один раз, выведите её индекс.
Если она встречается два и более раз, выведите индекс её первого и последнего вхождения на одной строке,
разделенных символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO».
"""

line = input()
el = 'f'
if line.count(el) == 0:
    print('NO')
elif line.count(el) == 1:
    print(line.index(el))
else:
    print(line.index(el), line.rindex(el))
