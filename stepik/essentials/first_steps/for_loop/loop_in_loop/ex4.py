n = int(input())
colors = [[int(el) for el in input().split()] for _ in range(n)]
homes = [colors[i][0] for i in range(n)]
guests = [colors[i][1] for i in range(n)]
count = 0
for h_color in homes:
    for g_color in guests:
        if h_color == g_color:
            count += 1
print(count)