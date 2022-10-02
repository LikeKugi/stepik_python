"""
На вход программе подается строка текста.
Напишите программу, которая определяет является ли введенная строка корректным телефонным номером.
Строка текста является корректным телефонным номером если она имеет формат:

abc-def-hijk
или
7-abc-def-hijk
где a, b, c, d, e, f, h, i, j, k – цифры от 0 до 9.
"""

phone_number = input().split('-')
flag = True
for i in range(len(phone_number)):
    if len(phone_number) == 4:
        if int(phone_number[0]) != 7:
            flag = False
            break
    if len(phone_number[i]) > 4:
        flag = False
        break
    if not phone_number[i].isdigit():
        flag = False
        break
    if -1 < i < len(phone_number) - 1:
        if len(phone_number[i])!=3 and len(phone_number)!=4:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')