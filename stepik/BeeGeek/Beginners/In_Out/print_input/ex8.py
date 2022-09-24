import itertools

number = input()
for i in itertools.permutations(number,3):
    print(*i,sep='')