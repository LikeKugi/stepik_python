from functools import reduce
number = int(input())
digits = []
while number > 0:
    digits += [number%10]
    number //=10
print(sum(digits))
multy = reduce((lambda x,y: x*y),digits)
print(multy)