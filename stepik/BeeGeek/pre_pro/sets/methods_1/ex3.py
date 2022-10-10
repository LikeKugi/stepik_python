# Напишите программу для определения общего количества различных слов в строке текста.
# Знаками препинания .,;:-?! пренебрегаем.

punctuation = {'.', ',', ';', ':', ';', '-', '?', '!'}

line = input().lower().split()
words = set()
for word in line:
    word = word.strip(".,;:-?!")
    words.add(word)
print(len(words))

print(len(set([el.strip(".,;:-?!") for el in input().lower().split()])))