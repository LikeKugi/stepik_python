#  Представьте, что у нас есть список целых чисел неограниченной вложенности.
#  То есть наш список может состоять из списков, внутри которых также могут быть списки.
#  Ваша задача превратить все это в линейный список при помощи функции flatten

def flatten(arr: list, result=None) -> list:
    if result is None:
        result = []
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            flatten(arr[i], result)
        else:
            result.append(arr[i])
    return result


print(flatten([1, [2, 3, [4]], 5]))
print(flatten([1, [2, 3], [[2], 5], 6]))
print(flatten([[[[9]]], [1, 2], [[8]]]))
