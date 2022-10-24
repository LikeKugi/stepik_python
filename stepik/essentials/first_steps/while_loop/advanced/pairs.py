boys_count = int(input())
boys_skillz = sorted(map(int, input().split()))

girls_count = int(input())
girls_skillz = sorted(map(int, input().split()))

max_pairs = min(boys_count, girls_count)
pairs = 0

print(boys_skillz)
print(girls_skillz)


def create_pair(ma_arr, mi_arr):
    if abs(ma_arr[-1] - mi_arr[-1]) <= 1:
        mi_arr.pop()
        ma_arr.pop()
        return 1
    else:
        ma_arr.pop()
        return 0


while boys_skillz and girls_skillz:
    if girls_skillz[-1] > boys_skillz[-1]:
        pairs += create_pair(girls_skillz, boys_skillz)
    else:
        pairs += create_pair(boys_skillz, girls_skillz)

print(pairs)
