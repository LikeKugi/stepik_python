"""
Дили Вили Били завели себе аккаунты в одной известной соцсети.
Их страницы стали пользоваться популярностью и, конечно же, появились поклонники, оставляющие комментарии.
Ребята решили узнать у кого из них самое большое количество уникальных комментаторов.
Ваша задача помочь им в этом и собрать нужную информацию.
"""

d = {'Дили' : set(), 'Вили' : set(),  'Били' : set()}
for s in iter(input, 'конец'):
    a, b = s.split(': ')
    d[a].add(b)
for x in d:
    d[x] = len(d[x])
for y, x in sorted(d.items(), key=lambda x: -x[1]):
    print(f'Количество уникальных комментаторов у {y} - {x}')