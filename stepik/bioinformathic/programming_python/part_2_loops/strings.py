genome = 'CACCTGGAC'

counter = 0
for i in range(len(genome)):
    if genome[i] == 'C':
        counter += 1
print('C times =', counter)

print('A times =', genome.count('A'))

s = 'aTGcc'
p = 'cc'

sLow = s.lower()
print(sLow)
sUp = s.upper()
print(sUp)
print(s.count(p))
print(s.find(p))
#  better choose
if p in s:
    print('yeah')
print(s.find('q'))  # -1 no match
sRep = s.replace('c', 'C')
print(sRep)

st = 'agTtcAGtc'
print(st.upper().count('gt'.upper()))