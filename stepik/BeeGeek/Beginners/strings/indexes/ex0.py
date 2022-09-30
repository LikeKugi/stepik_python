s = 'abcdefg'
print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')
print()
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s.index('w'))

print(*s[::-1],sep='\n')