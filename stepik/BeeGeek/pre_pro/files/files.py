from random import randrange as RR


with open(input(),'r') as inf:
    lines = list(map(str.rstrip, inf.readlines()))
    print(lines[RR(len(lines)-1)])