from collections import Counter


def frequencySort(s: str) -> str:
    sc = dict(Counter(s))
    print([k*v for k,v in sorted(list(sc.items()), key=lambda x: -x[1])])
    print(''.join([k*v for k,v in sorted(list(sc.items()), key=lambda x: -x[1])]))



frequencySort('tree')
frequencySort("Aabb")
