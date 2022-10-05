"""
На вход программе подается строка текста, содержащая символы.
Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.
"""

chars = [char for char in input().split()]
output_chars = list()
for char in chars:
    if len(output_chars) == 0 or char!=output_chars[-1][-1]:
        output_chars.append([char])
    else:
        output_chars[-1].append(char)
print(output_chars)