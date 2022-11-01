exceptions = {}

for _ in range(int(input())):
    line = input()
    if ' : ' in line:
        k, v = line.split(' : ')
        if ' ' in v:
            exceptions[k] = v.split()
        else:
            exceptions[k] = [v]
    else:
        exceptions[line] = []

print(exceptions)

stack = set()


def check_parents(query):
    if query in stack:
        return True
    if any(check_parents(el) for el in exceptions.get(query)):
        return True
    return False


for _ in range(int(input())):
    line = input()
    if line in set() or check_parents(line):
        print(line)
    stack.add(line)
