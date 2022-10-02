def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

x = 1
y = 7
print(x, y)
change_us(x, y)
print(x, y)

def print_text(text, num):
    while num > 0:
        print(text, end='')
        num -= 1

print_text('Python', 4)


print()
def swap(a, b):
    a, b = b, a

a = 4
b = 3
swap(a, b)
print(a - b)