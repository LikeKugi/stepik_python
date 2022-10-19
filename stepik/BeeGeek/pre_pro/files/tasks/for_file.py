"""
Вам доступен текстовый файл file.txt, набранный латиницей.
Напишите программу, которая выводит количество букв латинского алфавита, слов и строк.
Выведите три найденных числа в формате, приведенном в примере.
"""

with open('file.txt') as inf:
    count_lines = count_letters = count_words = 0
    for line in inf:
        count_lines += 1
        count_letters += len(list(el for el in line if el.isalpha()))
        count_words += len(line.split())

print(f'''Input file contains:
{count_letters} letters 
{count_words} words 
{count_lines} lines ''')
