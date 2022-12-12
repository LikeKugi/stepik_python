def get_max_subsequence(numbers: list):
    n = len(numbers)
    p = [0] * n
    M = [0] * (n + 1)
    L = 0
    for i in range(n):
        lo = 1
        hi = L
        while lo <= hi:
            mid = (lo + hi) // 2
            if numbers[M[mid]] < numbers[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        newL = lo
        p[i] = M[newL-1]
        M[newL] = i
        if newL > L:
            L = newL
    S = [0] * L
    k = M[L]
    for i in range(L-1, -1, -1):
        S[i] = numbers[k]
        k = p[k]
    return S




def main():
    length = int(input())
    sequence = list(map(int, input().split()))
    sub = get_max_subsequence(sequence)
    print(sub)


if __name__ == '__main__':
    main()
