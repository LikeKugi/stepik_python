#  По данным nn отрезкам необходимо найти множество точек минимального размера,
#  для которого каждый из отрезков содержит хотя бы одну из точек.
from collections import defaultdict


def get_int_numbers() -> map: return map(int, input().split())


def get_greedy(segments: list[tuple[int]]) -> list[int]:
    out_indexes = defaultdict(list)
    current = -1
    for segment in segments:
        if segment[0] > current:
            current = segment[1]
        out_indexes[current].append(segment)
    return list(out_indexes.keys())


def main():
    segmets = []
    for _ in range(int(input())):
        segmets.append(tuple(get_int_numbers()))
    segmets.sort(key=lambda x: x[1])
    answer = get_greedy(segmets)
    print(len(answer))
    print(*answer)


if __name__ == '__main__':
    main()
