x = [1,2,3]
print(id(x))
print(id([1,2,3]))

y = x

print(y is x)
print(y is [1,2,3])

print()

x = [1, 2, 3]
y = x
y.append(4)

s = "123"
t = s
t = t + "4"

print(str(x) + " " + s)