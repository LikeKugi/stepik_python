list1 = list(map(len, ['this', 'is', 'a', 'test']))
list2 = [len(word) for word in ['this', 'is', 'a', 'test']]

print(list1 == list2)

def is_a_student(score):
    return score > 75


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65, 75]
over_75 = list(filter(is_a_student, scores))

print(over_75)

def filter_vowels(letter):
    return letter in 'aeiou'


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

filtered_vowels = filter(filter_vowels, letters)

print(*filtered_vowels)

random_list = [1, 'a', 0, False, True, '0', 7, '']
filtered_list = list(filter(None, random_list))
print(filtered_list)

listA = [2, 3, 4]
listB = [3, 2, 1]

result = sum(map(pow, listA, listB))
print(result)