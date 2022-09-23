"""
Напишите программу, которая считывает из файла строку,
соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.
"""

with open ('dataset_3363_2 (1).txt') as inf:
    line = inf.readline()
print(line)
char = ''
times = ''
sum = ''
for el in line:
    if el.isalpha():
        if char != '' and times != '':
            sum+=char*int(times)
        times = ''
        char = el
    if el.isdigit():
        times += el
sum+=char*int(times)
with open('answer.txt','w') as ouf:
    ouf.write(sum)
