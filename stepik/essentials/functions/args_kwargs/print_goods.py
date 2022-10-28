#  Давайте теперь создадим функцию print_goods, которая печатает список покупок.
#  На вход она будет принимать произвольное количество значений, а товаром мы будем считать любые непустые строки.
#  То есть числа, списки, словари и другие нестроковые объекты вам нужно будет проигнорировать.
#  Функция print_goods должна печатать список товаров в виде:
#  <Порядковый номер товара>. <Название товара> (см. пример ниже).
#  В случае, если в переданных значениях не встретится ни одного товара, необходимо распечатать текст "Нет товаров"

def print_goods(*args):
    i = 1
    for arg in args:
        if isinstance(arg, str) and arg:
            print(f'{i}. {arg}')
            i += 1
    if i == 1:
        print('Нет товаров')

print_goods('apple', 'banana', 'orange')

print_goods(1, True, 'Грушечка', '', 'Pineapple')

print_goods([], {}, 1, 2)