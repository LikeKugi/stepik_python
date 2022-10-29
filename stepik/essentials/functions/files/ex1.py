#  Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное
#  слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной,
#  нужно вернуть слово, которое встречается последнее в тексте.

import string


def longest_word_in_file(f_name):
    with open(f_name, encoding='utf-8') as inf:
        words = inf.read().replace('\n', '').translate(str.maketrans('', '', string.punctuation)).split()
    max_len = 0
    long_word = ''
    for word in words:
        if len(word) >= max_len:
            long_word = word
            max_len = len(long_word)
    return long_word