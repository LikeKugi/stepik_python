"""
На вход программе подается строка генетического кода, состоящая из букв
    А (аденин),
    Г (гуанин),
    Ц (цитозин),
    Т (тимин).
Напишите программу, которая подсчитывает сколько
аденина, гуанина, цитозина и тимина входит в данную строку генетического кода.
"""

line = input().lower()
print(f"Аденин: {line.count('а')}")
print(f"Гуанин: {line.count('г')}")
print(f"Цитозин: {line.count('ц')}")
print(f"Тимин: {line.count('т')}")
