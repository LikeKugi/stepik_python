def merge_two_list(a, b):
    s = a[:] + b[:]

    s = quicksort(s)
    return s


# функция merge_sort должна выполнить сортировку
def merge_sort(s):
    return quicksort(s)


def quicksort(arrToSort):
    if len(arrToSort) < 2:
        return arrToSort
    else:
        pivot = arrToSort[0]
        less = [i for i in arrToSort[1:] if i <= pivot]
        greater = [i for i in arrToSort[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 18, 1, 2, 3, 4, 6, 8]))