s = 'foo goo moo'
print(s.count('oo'))
print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ

s = 'foobar'
print(s.startswith('foo'))  # начинается ли строка с подстроки
print(s.startswith('baz'))

print(s.endswith('bar'))  # заканчивается ли строка подстрокой
print(s.endswith('baz'))

s = 'foo bar foo baz foo qux'
print(s.find('foo'))  # поиск с начала строки
print(s.rfind('foo'))  # поиск с конца строки
print(s.find('bar'))
print(s.find('qu'))
print(s.find('python'))

s = '     foo bar foo baz foo qux      '
print(s.strip())  # удаляет пробелы в конце и в начале
print(s.lstrip())  # удаляет пробелы в начале
print(s.rstrip())  # удаляет пробелы в конце

s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault'))
s = 'foo bar foo baz foo qux'
print(s.replace('foo', 'grault', 2))  # опционально - количество замен