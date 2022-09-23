ouf = open('qet.txt','w')
ouf.write('test\n')
ouf.write(str(21214))
ouf.close()

inf = open('qet.txt','r')
s1 = inf.readline().strip()  # избавиться от whitespace в начале и конце строки
s2 = inf.readline()
inf.close()
print(s1)
print(s2)



with open('qet.txt', 'w') as ouf:
    ouf.write('here some text again\n')
    ouf.write(str(32))

with open('qet.txt') as inf:
    for line in inf:
        print(line.strip())