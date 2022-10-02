"""
На вход программе подается число n, а затем n строк, содержащих целые числа в порядке возрастания.
Из данных строк формируются списки чисел.
Напишите программу, которая объединяет указанные списки в один отсортированный список
с помощью функции quick_merge(), а затем выводит его.
"""


# объявление функции
def merge(list1, list2):
    result = list()
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1 if len(list1)!=0 else list2)
    return result


def quick_merge(list_total):
    result = list()
    for lists in list_total:
        result = merge(result, lists)
    return result


print(quick_merge([[1, 2, 3], [5, 6, 7, 8]]))
print(quick_merge([[1, 7, 10, 16], [5, 6, 13, 20], [1, 2, 3], [5, 6, 7, 8]]))


numbers = list()
for _ in range(int(input())):
    numbers.append([int(el) for el in input().split()])