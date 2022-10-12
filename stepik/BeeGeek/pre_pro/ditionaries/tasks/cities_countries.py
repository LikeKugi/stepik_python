"""
На вход программе подается список стран и городов каждой страны.
Затем даны названия городов. Напишите программу, которая для каждого города выводит, в какой стране он находится.

Формат входных данных
Программа получает на вход количество стран n.
Далее идет n строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
В следующей строке записано число m, далее идут m запросов — названия каких-то mm городов, из перечисленных выше.
"""

cities = {}
for _ in range(int(input())):
    country, *citi = input().split()
    cities.update(cities.fromkeys(citi, country))
for _ in range(int(input())):
    print(cities.get(input()))
