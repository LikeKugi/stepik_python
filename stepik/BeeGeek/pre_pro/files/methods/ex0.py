# seek() задаёт позицию курсора в байтах от начала файла.
# Чтобы перевести курсор в самое начало файла необходимо вызвать метод seek(),
# передав ему в качестве аргумента значение 0.

file = open('languages.txt', 'r', encoding='utf-8')
line1 = file.readline()
file.seek(0)               # переводим курсор в самое начало
line2 = file.readline()

print(line1 == line2)

file.close()