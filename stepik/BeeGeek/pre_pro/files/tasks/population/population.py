"""
Вам доступен текстовый файл population.txt с названиями стран и численностью их населения,
разделенными символом табуляции '\t'.

Напишите программу выводящую все страны, название которых начинается с буквы 'G', ч
исленность населения которых больше чем 500_000 человек, не меняя их порядок.
"""
countries = {}
with open('population.txt') as inf:
    for line in inf.readlines():
        name_country, population = map(str.rstrip, line.split('\t'))
        countries[name_country] = int(population)

for name, population in countries.items():
    if name.startswith('G') and population > 500_000:
        print(name)