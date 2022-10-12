"""
Вам доступен список pets, содержащий информацию о собаках и их владельцах.
Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).

Дополните приведенный код так, чтобы в переменной result хранился словарь,
в котором для каждого владельца будут перечислены его собаки.
Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца),
а значением – список кличек собак (сохранив исходный порядок следования).
"""

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for dog_name, owner_name, owner_last, owner_age in pets:
    if (owner_name, owner_last, owner_age) not in result:
        result[(owner_name, owner_last, owner_age)] = [dog_name]
    else:
        result[(owner_name, owner_last, owner_age)].append(dog_name)
print(result)
res1 = {}
for dog_name, *owner in pets:
    res1.setdefault((*owner,), []).append(dog_name)
print(res1)

print(res1==result)