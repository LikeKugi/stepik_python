#  Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе
#  Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
import csv
import collections


search_year = []
with open('Crimes.csv') as inf:
    df = csv.DictReader(inf)
    print(df)
    for row in df:
        if '2015' in row['Date']:
            search_year.append(row)

# print(search_year)
pr_type = {}
for row in search_year:
    pr_type[row.get('Primary Type')] = pr_type.setdefault(row.get('Primary Type'), 0) +1

print(max(pr_type,key=lambda x: pr_type.get(x)))
print(max(search_year,key=lambda x: search_year.count(x['Primary Type'])))
