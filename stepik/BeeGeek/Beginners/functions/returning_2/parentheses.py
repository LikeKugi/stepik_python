"""
Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую строку text,
состоящую из символов ( и ) и возвращает значение True если поступившая на вход строка является
правильной скобочной последовательностью и False в противном случае.

Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из символов
( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
"""


# объявление функции
def is_correct_bracket(text, opened='(', closed=')'):
    counter = 0
    for char in text:
        if char == opened:
            counter += 1
        if char == closed:
            counter -= 1
        if counter < 0:
            return False
    if counter != 0:
        return False
    return True


print(is_correct_bracket('()(()())'))
print(is_correct_bracket(')(())('))
