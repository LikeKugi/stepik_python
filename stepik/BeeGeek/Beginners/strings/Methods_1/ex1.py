"""
На вход программе подается строка состоящая из имени и фамилии человека,
разделенных одним пробелом. Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.
"""

line = input()
if line == line.title():
    print('YES')
else:
    print('NO')