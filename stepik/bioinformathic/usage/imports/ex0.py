GREETING = 'Hello, '

class BadName(Exception):
    pass


def greet(name:str) -> str:
    if name[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + 'is inappropriate name')


# имена для импорта
# from ex0 import *
__all__ = ['BadName', 'greet']