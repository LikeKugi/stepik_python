#  По данной непустой строке ss длины не более 10^4 , состоящей из строчных букв латинского алфавита,
#  постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k,
#  встречающихся в строке, и размер получившейся закодированной строки.
#  В следующих k строках запишите коды букв в формате "letter: code".
#  В последней строке выведите закодированную строку.
import collections
from collections import namedtuple
import heapq


class Node(namedtuple('Node', ['left', 'right'])):

    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):

    def walk(self, code, acc):
        code[self.char] = acc or '0'


def get_frequencies(s: str) -> dict:
    frequencies = collections.Counter(s)
    out = sorted(frequencies.items(), key=lambda x: -x[1])
    return frequencies


def create_encoding(frequencies: dict):
    h = []
    for ch, freq in frequencies.items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h

        root.walk(code, '')
    return code


def main():
    line = input()
    frequencies = get_frequencies(line)
    unique_chars = len(frequencies)

    encode = create_encoding(frequencies)

    encoded = ''.join([str(encode.get(char)) for char in line])
    print(unique_chars, len(encoded))
    for char in encode:
        print(f'{char}: {encode.get(char)}')
    print(encoded)


if __name__ == '__main__':
    main()
