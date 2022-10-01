"""
На вход программе подается натуральное число n, затем n строк,
затем еще одна строка — поисковый запрос.
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос.
"""

lines = list()
for _ in range(int(input())):
    lines.append(input())
query = input()
for line in lines:
    if query.lower() in line.lower():
        print(line)