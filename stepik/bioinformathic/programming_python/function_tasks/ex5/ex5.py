def average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)


class_height = {}
for i in range(1, 12):
    class_height[i] = []
with open('dataset_3380_5.txt') as inf:
    for line in inf:
        cl, name, height = line.split('\t')
        cl = int(cl)
        height = int(height)
        class_height[cl] += [height]
for key in class_height:
    print(key, average(class_height[key]) if len(class_height[key])>0 else '-')
