"""
В переменной students хранится словарь, содержащий информацию о росте (в см) и весе (в кг) студентов.

Дополните приведенный код, используя генератор, чтобы получить словарь result,
состоящий из всех элементов словаря students , где указан рост больше 167 см, а вес меньше 75 кг.
"""

students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50),
            'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78),
            'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
            'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

result = {name: data for name, data in students.items() if data[0] > 167 and data[1] < 75}

print(result)

result = {name: (height, weight) for name, (height, weight) in students.items() if height > 167 and weight < 75}

print(result)
