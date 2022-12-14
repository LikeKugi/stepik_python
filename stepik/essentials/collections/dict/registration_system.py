"""
Входные данные
В первой строке входных данных задано число n (1≤n≤105). Следующие n строк содержат запросы к системе.
Каждый запрос представляет собой непустую строку длиной не более 32 символов,
состоящую только из строчных букв латинского алфавита.

Выходные данные
В выходных данных должно содержаться n строк — ответы системы на запросы:
OK в случае успешной регистрации, или подсказку с новым именем, если запрашиваемое уже занято.
"""

names = set()


def check_name(name):
    i = 1
    while name in names:
        if (name+str(i)) not in names:
            return name+str(i)
        i += 1


for _ in range(int(input())):
    login = input()
    if login not in names:
        print('OK')
    else:
        login = check_name(login)
        print(login)
    names.add(login)