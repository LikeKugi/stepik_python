"""
На вход программе подается строка текста.
Напишите программу, которая выводит индекс второго вхождения буквы «f».
Если буква «f» встречается только один раз, выведите число -1, а если не встречается ни разу, выведите число -2.
"""

smb, line = 'f', input()
counter = 0
for i in range(len(line)):
    if line[i] == smb:
        counter+=1
        if counter == 2:
            print(i)
            break
else:
    if counter == 1:
        print(-1)
    else:
        print(-2)