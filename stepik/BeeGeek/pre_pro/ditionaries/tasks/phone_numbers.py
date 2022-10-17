"""
Формат входных данных
В первой строке задано одно целое число n — количество номеров телефонов,
информацию о которых Тимур сохранил в телефонной книге.
В следующих n строках заданы телефоны и имена их владельцев через пробел.
В следующей строке записано целое число m — количество поисковых запросов от Тимура.
В следующих m строках записаны сами запросы, по одному на строке.
Каждый запрос — это имя друга, чьи телефоны Тимур хочет найти.

Формат выходных данных
Для каждого запроса от Тимура выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем
(независимо от регистра имени).
Если в телефонной книге нет телефонов человека с таким именем,
выведите в соответствующей строке «абонент не найден» (без кавычек).

Примечание 1. Телефоны одного человека выводите в одну строку через пробел в том порядке,
в каком они были заданы во входных данных.
"""

phone_numbers = {}
error = 'абонент не найден'
for _ in range(int(input())):
    phone, name = input().lower().split()
    phone_numbers.setdefault(name,[]).append(phone)

for _ in range(int(input())):
    print(*phone_numbers.get(input().lower(), ['абонент не найден']))