"""
На вход программе подается натуральное число n и n строк с названиями файлов.
Напишите программу, которая создает файл output.txt
и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка.
"""

names = [input() for _ in range(int(input()))]

with open('output.txt', 'w') as ouf:
    for name in names:
        with open(name) as inf:
            for line in inf:
                ouf.write(line)
