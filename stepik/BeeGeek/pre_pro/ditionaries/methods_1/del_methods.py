# del можно удалять элементы словаря по определенному ключу.

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

del info['email']    # удаляем элемент имеющий ключ email
del info['job']      # удаляем элемент имеющий ключ job

print(info)

# pop() - Если требуется получить само значение удаляемого элемента

info = {'name': 'Sam',
        'age': 28,
        'job': 'Teacher',
        'email': 'timyr-guev@yandex.ru'}

email = info.pop('email')          # удаляем элемент по ключу email, возвращая его значение
job = info.pop('job')              # удаляем элемент по ключу job, возвращая его значение

print(email)
print(job)
print(info)

# popitem() удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа

info = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}

info['surname'] = 'Sinclar'

item = info.popitem()

print(item)
print(info)

# clear() удаляет все элементы из словаря

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info.clear()

print(info)

# copy() создает поверхностную копию словаря.

info = {'name': 'Bob',
        'age': 25,
        'job': 'Dev'}

info_copy = info.copy()
info_copy['name'] = 'TIM'

print(info)
print(info_copy)