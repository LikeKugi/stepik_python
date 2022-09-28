for i in range(1, 4):
    for j in range(3, 6):
        print(i, j)

for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')
print()
counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)