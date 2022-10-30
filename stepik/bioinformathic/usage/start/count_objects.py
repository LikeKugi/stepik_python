def counter(objects):
    return len(set(map(id, objects)))

print(counter([1, 2, 1, 2, 3]))
print(counter([1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]))