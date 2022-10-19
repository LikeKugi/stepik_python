"""
Вам доступен текстовый файл data.txt, в котором записаны строки текста.
Напишите программу, выводящую все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.
"""

with open('data.txt') as inf:
    print(*map(str.strip, inf.readlines()[::-1]),sep='\n')

print()

with open('data.txt', encoding='utf-8') as file:
    print(*file.readlines()[::-1], sep='')