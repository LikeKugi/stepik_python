"""
Напишите программу, которая с помощью модуля random генерирует n паролей длиной m символов,
состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
"""
import string
from random import randrange as rr

avoid_code = 'Il1oO0'
code = [el for el in string.ascii_uppercase + string.ascii_lowercase + string.digits]
for char in avoid_code:
    code.pop(code.index(char))

used_passwords = set()
count_psswords, length_passwords = int(input()), int(input())
while len(used_passwords) < count_psswords:
    password = ''.join([code[rr(len(code))] for el in range(length_passwords)])
    used_passwords.add(password)

print(*used_passwords, sep='\n')
