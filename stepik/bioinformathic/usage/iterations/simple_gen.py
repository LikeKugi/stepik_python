def simple_generator():
    print('checkpoint 1')
    yield 1
    print('checkpoint 2')
    yield 2
    print('checkpoint 3')
    return 'Text in StopIteration'


gen = simple_generator()
x = next(gen)
print(x)
y = next(gen)
print(y)
z = next(gen)  # StopIteration Exception