import math

n,a = int(input()), float(input())
s = (n * a**2) / (4*math.tan(math.pi/n))
print(s)