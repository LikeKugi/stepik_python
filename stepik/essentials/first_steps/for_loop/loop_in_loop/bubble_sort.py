"""
Все просто, вам поступает число n - количество элементов в списке, и затем сам список.

Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки,
в случае если элементы соседние совпадают менять их ненужно.

В качестве ответа нужно вывести отсортированный список и какое количество раз
пришлось переставлять элементы в процессе сортировки
"""

length = int(input())
numbers = list(map(int, input().split()))
counter = 0

for i in range(length - 1):
    current_counter = 0
    for j in range(length - i-1):
        if numbers[j] > numbers[j + 1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
            current_counter += 1
    counter += current_counter
    if current_counter == 0:
        break
print(counter)
print(*numbers)
