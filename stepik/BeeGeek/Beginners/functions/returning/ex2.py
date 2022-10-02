"""
Напишите функцию с именем find_all(target, symbol),
которая принимает два аргумента: строку target и символ symbol
и возвращает список, содержащий все местоположения этого символа в строке.

Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.
"""

# объявление функции
def find_all(target, symbol):
    return [index for index in range(len(target)) if target[index] == symbol]

print(find_all('abcdabcaaa', 'a'))
print(find_all('abcadbcaaa', 'e'))
print(find_all('abcadbcaaa', 'd'))

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))