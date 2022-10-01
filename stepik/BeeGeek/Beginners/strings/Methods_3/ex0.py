s = 'aabbAA111ccDDaa'
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

s = 'aabb!@#$11cc'
print(s.islower())

s = '    abbc    '
print(s.isspace())

# форматирование строк
age = 27
txt = 'My name is Timur, I am {}'.format(age)
print(txt)

age = 27
name = 'Timur'
profession = 'math teacher'
txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
print(txt)

s = 'In {0}, someone paid {1} {2} for two pizzas.'
print(s.format(2010,'10k','Bitcoin'))