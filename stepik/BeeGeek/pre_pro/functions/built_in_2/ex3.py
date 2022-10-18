"""
Используя параллельную итерацию сразу по трем спискам countries, capitals и population выведите информацию о стране
"""

countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for country, capital, people in zip(countries,capitals,population):
    print(f'{capital} is the capital of {country}, population equal {people} people.')