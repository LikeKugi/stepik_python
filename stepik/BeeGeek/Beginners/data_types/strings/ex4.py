cities = []
for _ in range(3):
    cities.append(input())
max_index = min_index = 0
for i in range(len(cities)):
    if len(cities[i]) > len(cities[max_index]):
        max_index = i
    elif len(cities[i]) < len(cities[min_index]):
        min_index = i
print(cities[max_index], cities[min_index], sep='\n')
