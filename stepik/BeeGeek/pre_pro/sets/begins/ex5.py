# На вход программе подается строка, состоящая из трех слов.
# Верно ли, что для записи всех трех слов был использован один и тот же набор букв?

words = list(input().split())
print(('NO', 'YES')[set(words[0]) == set(words[1]) == set(words[2])])
