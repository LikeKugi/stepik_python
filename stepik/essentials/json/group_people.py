import json

with open('group_people.json') as inf:
    data = json.load(inf)

print(*data,sep='\n')
totals = []
for line in data:
    print(line['id_group'])
    peoples = [el for el in line['people'] if el['gender'] == 'Female' and el['year']>1977]
    print(peoples)
    totals.append([line['id_group'], peoples])

for total in totals:
    print(total[0], len(total[1]))

print(*max(totals,key=lambda x: len(x[1])))
a,b = max(totals,key=lambda x: len(x[1]))
print(a,len(b))