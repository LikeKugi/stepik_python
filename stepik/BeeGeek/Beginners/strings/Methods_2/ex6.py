"""
На вход программе подается строка текста.
Напишите программу, которая выводит на экран символ, который появляется наиболее часто.
"""
line = input()
char = ''
counts = 0
for el in line:
    if line.count(el)>= counts:
        char = el
        counts = line.count(char)
print(char)