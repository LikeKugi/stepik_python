numbers = [10, 20, 30, 40, 50]
print(numbers[-2])
print(numbers[-4:-1])
print('-------------------------------')
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[2:5])
print(numbers[:4])
print(numbers[3:])
print('-------------------------------')
numbers = [4, 8, 12, 16, 34, 56, 100]
numbers[1:4] = [20, 24, 28]
print(numbers)
print('-------------------------------')
numbers = [5, 10, 15, 25]
print(numbers[::-2])
print('-------------------------------')
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)

numbers.append(60)
print(numbers)
print('-------------------------------')
numbers = [10, 20, 30, 40, 50]
numbers.pop()
print(numbers)

numbers.pop(2)
print(numbers)
print('-------------------------------')
words = ['Hello', 'Python']
print('-'.join(words))
print('-------------------------------')
numbers = [10, 20, 30, 40]
del numbers[0:6]
print(numbers)
print('-------------------------------')
words = ['xyz', 'zara', 'beegeek']
print(max(words))
print('-------------------------------')
numbers = [1, 2, 3, 4, 5, 6, 7]
new_numbers =  [2 * x for x in numbers]
print(new_numbers)
print('-------------------------------')