"""
На вход программе подается строка текста.
Напишите программу, которая подсчитывает количество цифр в данной строке.
"""
counter = 0
for el in input():
    if el.isdigit():
        counter += 1
print(counter)

print(sum(i.isdigit() for i in input()))