d = dict(foo=100, bar=200, baz=300)
print(d)

d = {('foo', 100), ('bar', 200), ('baz', 300)}
print(d)
d = {}
d['foo'] = 100
d['bar'] = 200
d['baz'] = 300
print(d)
d = {'foo': 100, 'bar': 200, 'baz': 300}
print(d)

d = dict([('foo', 100), ('bar', 200), ('baz', 300)])
print(d)

data = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
        {
            'x' : 10,
            'y' : 20,
            'z' : 30
        },
        'baz': 3
    },
    'c',
    'd'
]