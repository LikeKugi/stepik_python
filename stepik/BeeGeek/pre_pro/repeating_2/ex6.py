"""
Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
"""

line = input().upper()
counter = 0
max_times = 0
for i in line:
    if i == 'Р':
        counter += 1
    else:
        if counter > max_times:
            max_times = counter
        counter = 0
if counter > max_times:
    max_times = counter
print(max_times)
