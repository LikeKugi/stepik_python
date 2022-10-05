"""
На вход программе подаются две строки, на одной символы, на другой число n. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков указанной длины.
"""

"""
chars = [el for el in input().split()]
n = int(input())
temp, output = list(), list()
for i in range(len(chars)):
    temp.append(chars[i])
    if len(temp) == n or i == len(chars)-1:
        output.append(temp.copy())
        temp.clear()
print(output)
"""

def chunked(sp, n):
    return [sp[x:x + n] for x in range(0,len(sp),n)]


s = input().split()
n = int(input())
print(chunked(s, n))