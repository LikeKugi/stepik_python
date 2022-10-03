"""
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова
word1 и word2 и возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе
и False в противном случае.
"""


# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        flag = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                flag += 1
            if flag == 2:
                return False
        if flag == 1:
            return True
    return False


print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))
