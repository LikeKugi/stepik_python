"""
Дополните приведенный код, используя генератор, так, чтобы получить словарь result ,
в котором ключом будет строка – элемент списка words, а значением –
список соответствующих кодов ASCII символов данной строки.
"""

words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {word:[ord(char) for char in word] for word in words}

print(result)