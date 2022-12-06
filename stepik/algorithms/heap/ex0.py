import heapq

heap = []

variants = {
    'Insert': heapq.heappush,
    'ExtractMax': heapq.heappop
}


def main():
    for _ in range(int(input())):
        line = input()
        if line in variants:
            print(f'extract: {abs(variants.get(line)(heap))}')
        else:
            move, value = line.split()
            value = int(value)
            variants.get(move)(heap, -value)
            heapq.heapify(heap)
            print('pushing', end=' ')
            print(value)


if __name__ == '__main__':
    main()
