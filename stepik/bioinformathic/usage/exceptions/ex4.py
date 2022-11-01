class BadNameException(Exception):
    pass

def greet(name:str):
    if name[0].isupper():
        return f'Hello, {name}'
    else:
        raise BadNameException(f'bad name exception: {name} isnt good')

try:
    print(greet('adam'))
except Exception as e:
    print(f'no {e}')

print(greet('Adam'))