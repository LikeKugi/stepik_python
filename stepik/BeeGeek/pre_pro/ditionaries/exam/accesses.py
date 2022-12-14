"""
Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).
Напишите программу для восстановления контроля прав доступа к файлам.
Ваша программа для каждого запроса должна будет возвращать
OK если выполняется допустимая операция,
и Access denied, если операция недопустима.

Формат входных данных
Программа получает на вход количество файлов n, содержащихся в файловой системе компьютера.
Далее идет n строк, на каждой имя файла и допустимые с ним операции, разделенные символом пробела.
В следующей строке записано число m — количество запросов к файлам, и затем mm строк с запросами вида операция файл.
Одному и тому же файлу может быть адресовано любое количество запросов.

Формат выходных данных
Программа должна вывести для каждого из mm запросов в отдельной строке Access denied или OK.
"""

files = {}
permissions = {'write': 'W', 'read': 'R', 'execute': 'X'}

for _ in range(int(input())):
    name, *ds = input().split()
    files.setdefault(name, []).extend(ds)

for _ in range(int(input())):
    query, file = input().split()
    if permissions.get(query) in files.get(file):
        print('OK')
    else:
        print('Access denied')