students = ['ivan', 'masha', 'sasha']
for student in students:
    print('Hello,', student.title() + '!')

teachers = ['oleg', 'alex']
boys = students+teachers
for boy in boys:
    print(boy.title(),end=' ')
print()

boys.append('olga')
boys += ['boris', 'sergey']
for boy in boys:
    print(boy.title(),end=' ')
print()

boys.insert(1, 'mikola')
for boy in boys:
    print(boy.title(),end=' ')
print()

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(len(students))
students.remove('O')
del students[-1]
for student in students:
    print(student.title(), end=' ')
print()

if 'g' in students:
    print('here')
    students.remove('g')
if 'Ann' not in students:
    students.append('Ann')
for student in students:
    print(student.title(), end=' ')
print()

ordered_students = sorted(students)
print(ordered_students)
print(ordered_students[::-1])

new_list_students = ordered_students.copy()
new_list_students[0] = 'hello'
print(ordered_students)
print(new_list_students)

a = [1, 2, 3]
b = a
for i in b:
    print(i,' ',end='')
print(';',end='')
# значения списка b?

a[1] = 10
for i in b:
    print(i,' ',end='')
print(';',end='')
# значения списка b?

b[0] = 20
for i in a:
    print(i,' ',end='')
print(';',end='')
# значения списка a?

a = [5, 6]
for i in b:
    print(i,' ',end='')
print(';',end='')
# значения списка b?

print()
a = [[0]*4]*4
print(a)
a[0][0] = 5  # a - список ссылок на a[0]
print(a)