def greet(name:str):
    if name[0].isupper():
        return f'Hello, {name}'
    else:
        raise ValueError(f'{name} isnt good')

try:
    print(greet('adam'))
except Exception as e:
    print('no')

print(greet('Adam'))