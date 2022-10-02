numbers = [1, 2, 3, 4, 5]
numbers[2] = 99
print(numbers)

numbers = list(range(3))
print(numbers)

numbers = [10] * 5
print(numbers)

numbers = list(range(1, 10, 2))
for i in numbers:
    print(i, end='*')
print()

numbers = [1, 2, 3, 4, 5]
print(numbers[-2])

numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
numbers3 = numbers1 + numbers2
print(numbers3)

numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:3]
print(my_list)

numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:]
print(my_list)

numbers = [1, 2, 3, 4, 5]
my_list = numbers[:-1]
print(my_list)

numbers = [1, 2, 3, 4, 5]
my_list = numbers[:]
print(my_list)

names = ['Джим', 'Джилл', 'Джон', 'Джасмин']
if 'Джасмин' not in names:
    print ('Не могу найти Джасмин.')
else:
    print('Ceмья Джасмин: ', end='')
    print(names)