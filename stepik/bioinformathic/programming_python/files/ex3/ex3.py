def avar(numbers):
    s = 0
    for number in numbers:
        s += int(number)
    return s / len(numbers)

math = []
phys = []
russian = []
pupils = {}
with open('dataset_3363_4 (1).txt') as inf:
    for line in inf:
        name, m, p, r = line.replace('\n', '').split(';')
        pupils[name] = (int(m) + int(p) + int(r)) / 3
        math.append(m)
        phys.append(p)
        russian.append(r)
print(math)
print(phys)
print(russian)
with open('answer.txt', 'w') as ouf:
    for name in pupils:
        print(pupils[name], file=ouf)
    print(avar(math), avar(phys), avar(russian), file=ouf)
