#  Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
#  (Такая пара элементов называется инверсией массива.
#  Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
#  например, в упорядоченном по не убыванию массиве инверсий нет вообще,
#  а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
class MergeSort:

    def __init__(self, numbers):
        self.numbers = numbers
        self.inversions = 0

    def merge(self, left: list, right: list) -> list:
        n, m = len(left), len(right)
        result = []
        i, j = 0, 0
        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                self.inversions += (n - i)
                result.append(right[j])
                j += 1
        result.extend(left[i:] or right[j:])

        return result

    def merge_sort(self, numbers: list) -> list:
        n = len(numbers)
        if n < 2:
            return numbers[:]

        m = n // 2
        left = self.merge_sort(numbers[:m])
        right = self.merge_sort(numbers[m:])
        numbers = self.merge(left, right)
        return numbers

    def __call__(self, *args, **kwargs):
        self.merge_sort(self.numbers)
        return self.inversions


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    merging = MergeSort(numbers)
    print(merging())


if __name__ == '__main__':
    main()
