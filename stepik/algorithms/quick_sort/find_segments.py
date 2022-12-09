#  В первой строке задано два целых числа - количество отрезков и точек на прямой, соответственно.
#  Следующие nn строк содержат по два целых числа a и b координаты концов отрезков.
#  Последняя строка содержит mm целых чисел — координаты точек.
#  Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
#  Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
from bisect import bisect, bisect_left, bisect_right


def get_int_values(): return tuple(map(int, input().split()))


def main():
    count_lines, count_points = get_int_values()
    segments = []
    for _ in range(count_lines):
        segments.append(get_int_values())
    segments.sort(key=lambda x: (x[0], x[1]))
    starts = sorted(x[0] for x in segments)
    ends = [x[1] for x in sorted(segments, key=lambda x: x[1])]
    print(starts, ends)
    print(segments)
    points = get_int_values()
    for point in points:
        print('/------------------------------------------------------------------------------/')
        print(len(tuple(filter(lambda x: x[0] <= point <= x[1], segments))))
        print(segments)
        print(f'point: {point}')
        i = bisect_left(ends, point)
        j = bisect_right(starts, point)
        print(f'{i=} {j=}')
        print(abs(i-j))

        print()


if __name__ == '__main__':
    main()
