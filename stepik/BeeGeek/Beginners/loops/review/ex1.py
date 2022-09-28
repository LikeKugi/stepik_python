max_negative = 0
sum_negative = 0
for _ in range(10):  # 1 - range(10)
    x = int(input())
    if x < 0:
        if max_negative == 0:
            max_negative = x
        sum_negative += x  # 2 - s += x
        if x > max_negative:  # 3 - tab
            max_negative = x
print(sum_negative)
print(max_negative)