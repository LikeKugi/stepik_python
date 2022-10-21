"""
Однажды Жака Фреско спросили:

"Если ты такой умный, почему не богатый?"

Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:

"Были разноцветные козлы. Сколько?"

"Сколько чего?"

"Сколько из них составляет более 7% от общего количества козлов?"

Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS,
далее идет список всех возможных цветов козлов. Затем идет строка со словом GOATS,
и далее непосредственно перечисление козлов разных цветов. Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов,
которые удовлетворяют условию загадки от Жака Фреско.
"""
colours = {}
with open('goats.txt') as inf:
    line = ''
    while line != 'GOATS':
        line = inf.readline().rstrip()

        if line not in ('COLOURS', 'GOATS'):
            colours.setdefault(line, 0)
    for line in inf.readlines():
        colours[line.rstrip()] += 1

total = sum(colours.values())

answer = sorted(filter(lambda x: int(colours[x]) > (total / 100) * 7, colours))

with open('answer.txt', 'w') as ouf:
    print(*answer,sep='\n',file=ouf)


