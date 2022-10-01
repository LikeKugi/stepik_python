"""
На вход программе подается натуральное число n, затем n строк,
затем число k — количество поисковых запросов, затем k строк — поисковые запросы.
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
"""

lines = [input() for _ in range(int(input()))]
queries = [input().lower() for _ in range(int(input()))]
for line in lines:
    for query in queries:
        if query not in line.lower():
            break
    else:
        print(line)