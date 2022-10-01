"""
На вход программе подается строка текста.
Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.
"""
line = input()
ends = ['.ru', '.com']
for i in ends:
    if line.endswith(i):
        print('YES')
        break
else:
    print('NO')