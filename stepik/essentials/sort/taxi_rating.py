# Входные данные
# Программа будет принимать строки, в которых сперва указывается имя таксиста,
# а затем через запятую с пробелом его оценка за заказ.
#
# Строка "конец" является последней строкой и означает окончание ввода
#
# Выходные данные
# Нужно расположить таксистов в порядке убывания их средней оценке и вывести имя каждого таксиста
# и его среднюю оценку в отдельной строке. В случае совпадения средних оценок расположить таксистов
# нужно отсортировать имена таксистов по алфавиту
from collections import defaultdict
drivers = defaultdict(list)

for line in iter(input, 'конец'):
    name, rating = line.split(', ')
    drivers[name].append(int(rating))
for driver in drivers:
    drivers[driver] = sum(drivers[driver])/len(drivers[driver])

print(*[f'{k} {drivers[k]}' for k in sorted(drivers,key=lambda x: -drivers[x])],sep='\n')