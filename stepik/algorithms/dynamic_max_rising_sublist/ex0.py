# Дано целое число 1 ≤ n ≤ 10^3 и массив A[1…n] натуральных чисел, не превосходящих 2 * 10^9.
# Выведите максимальное 1 ≤ k ≤ n, для которого найдётся подпоследовательность 1 ≤ i_1 ≤ i_2 ≤ ... ≤ i_k ≤ n  длины k,
# в которой каждый элемент делится на предыдущий
def get_max_subsequence(numbers: list) -> int:
    n = len(numbers)
    subsequences = [0] * n

    for i in range(n):
        subsequences[i] = 1
        for j in range(i):
            if (not numbers[i] % numbers[j]) and subsequences[j] + 1 > subsequences[i]:
                subsequences[i] = subsequences[j] + 1
    return max(subsequences)


def main():
    length = int(input())
    numbers = list(map(int, input().split()))
    max_length = (get_max_subsequence(numbers))
    print(max_length)


if __name__ == '__main__':
    main()
