with open(input()) as inf:
    print(*map(str.strip, inf.readlines()[-10:]),sep='\n')
