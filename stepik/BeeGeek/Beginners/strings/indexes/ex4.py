"""
На вход программе подается одна строка с буквами русского языка.
Напишите программу, которая определяет количество гласных и согласных букв.
"""

vowels = 0
consonants = 0
line = input()
el_vowel = 'ауоыиэяюёе'
el_consonants = 'бвгджзйклмнпрстфхцчшщ'

for char in line:
    if char.lower() in el_vowel:
        vowels += 1
    elif char.lower() in el_consonants:
        consonants += 1
print(f'Количество гласных букв равно {vowels}')
print(f'Количество согласных букв равно {consonants}')
