"""
У нас в наличии рюкзак, вместимость которого составляет n литров, и наша задача забить его до предела
максимально возможно. Нам поступают вещи, объем которых измеряется также в литрах, и мы должны их складывать
в наш рюкзак без возможности пропуска. Как только суммарный объем новой добавляемой вещи превысит вместимость рюкзака,
ваша программа должна вывести слово "Довольно!" и затем на отдельных строчках суммарный объем вещей,
которые мы смогли упаковать в рюкзак, и их количество
"""

value = int(input())
counter = 0
current_value = 0
while current_value < value:
    n = int(input())
    if n + current_value > value:
        break
    current_value += n
    counter += 1

print('Довольно!')
print(current_value)
print(counter)