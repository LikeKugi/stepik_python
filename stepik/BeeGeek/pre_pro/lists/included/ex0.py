list1 = [[1, 8, 9], [4, 8, 12, 16], [0, 2, 7]]
print(list1[0][1] + list1[1][2] + list1[2][2])

list1 = [[1, 8, 9], [4, 8, 12, 16], [0, 2, 7]]
#print(list1[0][1] + list1[3][2] + list1[2][2])
print()
list1 = ['Beegeek', [4, 8, 12, 16]]
print(list1[0][1])
print(list1[1][3])
print()
list1 = [[0, [9, 2]], [1, [4, 6, 3], [5, 2, 3], 8, 3]]
print(list1[1][2][1])
print()

list1 = [[1] * 3] * 3
list1[0][1] = 5
print(list1[1][1])
print()

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum + minimum)
print()

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum)