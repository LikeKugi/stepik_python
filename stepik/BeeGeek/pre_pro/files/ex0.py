with open('nums.txt','r') as inf:
    print(sum(map(int, inf.read().split())))