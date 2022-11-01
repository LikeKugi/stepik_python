try:
    x = [1,2,'hello',7]
    x.sort()
except TypeError:
    print('Type err :(')
print(x)