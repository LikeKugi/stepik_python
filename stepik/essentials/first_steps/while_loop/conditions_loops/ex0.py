t = 7
while t > 1:
    t -= 1
    if t == 3:
        break
    print(t)

print()

t = 7
while t > 1:
    t -= 1
    if t == 3 or t == 1:
        continue
    print(t)