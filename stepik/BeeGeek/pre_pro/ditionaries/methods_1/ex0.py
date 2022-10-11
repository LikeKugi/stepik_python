# update - реализует своеобразную операцию конкатенации для словарей

info1 = {'name': 'Bob',
         'age': 25,
         'job': 'Dev'}

info2 = {'age': 30,
         'city': 'New York',
         'email': 'bob@web.com'}

info1.update(info2)

print(info1)
# --------------------------------------------------------------------
info1 = {'name': 'Bob',
         'age': 25,
         'job': 'Dev'}

info2 = {'age': 30,
         'city': 'New York',
         'email': 'bob@web.com'}

info1 |= info2

print(info1)

# setdefault - позволяет получить значение из словаря по заданному ключу,
# автоматически добавляя элемент словаря, если он отсутствует.

info = {'name': 'Bob',
        'age': 25}

name1 = info.setdefault('name')  # параметр default не задан
name2 = info.setdefault('name', 'Max')  # параметр default задан

print(name1)
print(name2)
# --------------------------------------------------------------------
info = {'name': 'Bob',
        'age': 25}

job = info.setdefault('job', 'Dev')
print(info)
print(job)
# --------------------------------------------------------------------
info = {'name': 'Bob',
        'age': 25}

job = info.setdefault('job')
print(info)
print(job)