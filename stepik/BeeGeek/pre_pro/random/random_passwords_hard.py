"""
Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра
и как минимум по одной букве в верхнем и нижнем регистре.
"""

import string
from random import randrange as rr


def generate_password(length):
    used = [False, False, False]
    pswd = ''
    while False in used:
        i = rr(len(used))
        if used[i] == True:
            continue
        used[i] = True
        pswd += code[i][rr(len(code[i]))]
    while len(pswd) < length:
        i = rr(len(code))
        pswd += str(code[i][rr(len(code[i]))])
    return pswd


def generate_passwords(count, length):
    used_passwords = set()
    for _ in range(count):
        used_passwords.add(generate_password(length))
    return used_passwords


def create_code():
    avoid_code = 'Il1oO0'
    possible_alpha = list()
    possible_alpha.append([el for el in string.ascii_uppercase if el not in avoid_code])
    possible_alpha.append([el for el in string.ascii_lowercase if el not in avoid_code])
    possible_alpha.append([el for el in string.digits if el not in avoid_code])
    return possible_alpha


code = create_code()
n, m = int(input()), int(input())

print(*generate_passwords(n, m), sep='\n')
