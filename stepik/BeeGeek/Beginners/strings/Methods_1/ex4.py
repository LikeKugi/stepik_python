"""
На вход программе подается строка.
Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
"""

line = input()
counter = 0
for el in line:
    if el.islower():
        counter+=1
print(counter)