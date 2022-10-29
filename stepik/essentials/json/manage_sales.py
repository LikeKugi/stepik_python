import json

with open('manager_sales.json') as inf:
    data = json.load(inf)

print(*data, sep='\n')
print(type(data))
total = []
for line in data:
    print(line['manager']['first_name'],line['manager']['last_name'])
    sales = [el for val in line['cars'] for k,el in val.items() if k == 'price']
    print(sales)
    total.append([line['manager']['first_name'],line['manager']['last_name'],sum(sales)])

print(total)
print(*max(total,key=lambda x: x[2]))