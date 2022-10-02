"""
Напишите функцию merge(list1, list2), которая принимает в качестве аргументов
два отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.

Примечание 1. Списки list1 и list2 могут иметь разную длину.

Примечание 2. Можно использовать списочный метод sort(), а можно обойтись и без него 😎.
"""


# объявление функции
def merge(list1, list2):
    result = list()
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1)
    result.extend(list2)
    return result


print(merge([1, 2, 3], [5, 6, 7, 8]))
print(merge([1, 7, 10, 16], [5, 6, 13, 20]))

"""
# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
"""
