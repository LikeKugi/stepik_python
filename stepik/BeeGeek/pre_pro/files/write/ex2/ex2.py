"""
Напишите программу, которая считывает строку текста и записывает её в текстовый файл output.txt.
"""

with open('output.txt', 'w') as ouf:
    print(input(), file=ouf)
