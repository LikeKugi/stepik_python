def twoSum(numbers: list[int], target: int) -> list[int]:
    n = len(numbers)
    used = set()
    for i in range(n - 1):
        if numbers[i] in used:
            continue
        for j in range(i + 1, n):
            used.add(numbers[i])
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
