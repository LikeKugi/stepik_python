words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')  # добавить строкой
words2.extend('python')  # добавить списком

print(words1)
print(words2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]  # удалить эл-ты из списка

print(numbers)