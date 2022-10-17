"""
Напишите программу, переводящую цепь ДНК в цепь РНК.

Формат входных данных
На вход программе подается корректная цепь ДНК в верхнем регистре.

Формат выходных данных
Программа должна вывести соответствующую цепь РНК в верхнем регистре.
"""

rna_key = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
for gen in input():
    print(rna_key.get(gen),sep='',end='')