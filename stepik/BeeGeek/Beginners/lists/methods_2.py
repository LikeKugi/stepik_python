names = ['Gvido', 'Roman' , 'Timur']
print(names)
names.insert(0, 'Anders')  # встатвить на заданное место
print(names)
names.insert(3, 'Josef')
print(names)

food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')  # Удалить первый подходящий элемент
print(food)

names = ['Gvido', 'Roman' , 'Timur']
item = names.pop(1)  # удалить элемент из списка и вернуть его
print(item)
print(names)