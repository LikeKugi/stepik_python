"""
Вам доступен текстовый файл lines.txt, в котором записаны строки текста.
Напишите программу, которая выводит все строки наибольшей длины из файла, не меняя их порядок.
"""

with open('lines.txt') as inf:
    lines = list(map(str.strip, inf.readlines()) )
    #print(lines)
    #max_len = len(max(lines, key=len))
    #print(max_len)
    print(*filter(lambda x: len(x) == len(max(lines, key=len)), lines),sep='\n')
