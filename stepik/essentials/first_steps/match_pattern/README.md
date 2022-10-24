https://peps.python.org/pep-0622/
```python
a = input()  # or smth else
match a:
    case 'value_1':
        pass
    case 'value_2':
        pass
    case _:  # like Default or no cases choosen
        pass
```