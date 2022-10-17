"""
Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов
(любая непустая строка) по образцу: <номер продукта>)
<название продукта> (нумерация продуктов начинается с единицы).
Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.

Примечание 1. Обратите внимание, что функция должна принимать не список, а именно произвольное количество аргументов.

Примечание 2. Числа, списки, кортежи, словари, множества и другие нестроковые объекты продуктами не являются
и их нужно игнорировать.
"""

def print_products(*args):
    groceries = [el for el in args if el and type(el) in (str,)]
    if len(groceries) == 0:
        print('Нет продуктов')
        return
    for i in range(len(groceries)):
        print(f'{i+1}) {groceries[i]}')




print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')