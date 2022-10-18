"""
На вход программе подается натуральное число n, а затем n строк английских слов в разных регистрах.

Напишите программу, которая выводит слова в начальном регистре (каждое на отдельной строке)
в порядке возрастания их гематрии. Если гематрия слов совпадает,
они выводятся в алфавитном (лексикографическом) порядке.
"""

words = [input() for _ in range(int(input()))]
#print(words)
for word in words:
    print(sum([ord(el)-ord('A') for el in word.upper()]))
print(*sorted(words, key=lambda x: (sum([ord(el)-ord('A') for el in x.upper()]),x)),sep='\n')
