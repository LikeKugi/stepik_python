"""
На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python.
Напишите программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий.
Будем считать, что любая строка, начинающаяся со слова def и пробела, является началом определения функции.
Функция содержит комментарий, если первый символ предыдущей строки - #.
"""
counter = 0
with open(input()) as inf:
    code = inf.readlines()
    for i in range(len(code)):
        if code[i].startswith('def') and (not code[i-1].startswith('#') or i == 0):
            print(code[i][code[i].find('f ')+2:code[i].find('(')])
            counter +=1

if counter == 0:
    print('Best Programming Team')