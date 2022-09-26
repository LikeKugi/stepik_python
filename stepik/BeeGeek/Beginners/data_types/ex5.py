numbers = []
for i in range(5):
    numbers.append(int(input()))
print('Наименьшее число =', min(numbers))
print('Наибольшее число =', max(numbers))

for i in range(3):
    numbers.append(i*10)    #(int(input()))
numbers.sort(reverse=True)
print(*numbers,sep='\n')