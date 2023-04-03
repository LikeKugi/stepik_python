# Расстановка скобок в коде
from typing import TypeVar

_T = TypeVar('_T', int, str)


def check_brackets(line: str = '') -> _T:
    brackets_opening = {
        '{': '}',
        '(': ')',
        '[': ']'
    }
    brackets_closing = {v: k for k, v in brackets_opening.items()}
    stack = []
    for i, char in enumerate(line):
        if char in brackets_opening.keys():
            stack.append((char, i))
        elif char in brackets_closing.keys():
            if len(stack) > 0 and stack[-1][0] == brackets_closing[char]:
                stack.pop()
            else:
                return i + 1
    if len(stack) == 0:
        return 'Success'
    return stack[0][1] + 1


print(check_brackets('()[]({})'))

print(check_brackets('{}[]'))
print(check_brackets('[()]'))
print(check_brackets('(())'))
print(check_brackets('{[]}()'))
print(check_brackets('{'), 1)
print(check_brackets('{[}'), 3)
print(check_brackets('foo(bar)'))
print(check_brackets('foo(bar[i)'), 10)
print(check_brackets('{{[()]]'), 7)
print(check_brackets('()[]}'), 5)
print(check_brackets('{}([]'), 3)
