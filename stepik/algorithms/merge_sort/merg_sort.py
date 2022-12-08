#  Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
#  (Такая пара элементов называется инверсией массива.
#  Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
#  например, в упорядоченном по не убыванию массиве инверсий нет вообще,
#  а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
class MergeSort:
    """
    Merge sort of a list of numbers
    """

    def __init__(self, numbers: list[int | float]) -> None:
        """
        sort a list of numbers with a merge sort.\n
        if call the function it will return count of inversions in the list.\n
        :param numbers: list[int | float]
        """
        self.numbers: list[int | float] = numbers
        self.inversions: int = 0

    def merge(self, left: list[int | float], right: list[int | float]) -> list[int | float]:
        n, m = len(left), len(right)
        result: list[int | float] = []
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

    def merge_sort(self, numbers: list[int | float]) -> list[int | float]:
        n = len(numbers)
        if n < 2:
            return numbers[:]

        m = n // 2
        left = self.merge_sort(numbers[:m])
        right = self.merge_sort(numbers[m:])
        numbers = self.merge(left, right)
        return numbers

    def __call__(self, *args, **kwargs) -> int:
        """
        merge sort a list
        :param args: no need
        :param kwargs: no need
        :return: int
            count of inversions in the list
        """
        self.merge_sort(self.numbers)
        return self.inversions


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    merging = MergeSort(numbers)
    print(merging())


if __name__ == '__main__':
    main()
