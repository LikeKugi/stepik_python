sentence = 'The cat in the hat had two sidekicks, thing one and thing two.'

words = sentence.lower().replace('.', '').replace(',', '').split()

vowels = ['a', 'e', 'i', 'o', 'u']

consonants = {frozenset({letter for letter in word if letter not in vowels}) for word in words}

print(*consonants, sep='\n')

set1 = frozenset('beegeek')
set2 = frozenset('stepik')

set3 = set1 | set2
print(set3)

set1 = frozenset('beegeek')
set2 = frozenset('stepik')

set3 = set1 & set2
print(set3)