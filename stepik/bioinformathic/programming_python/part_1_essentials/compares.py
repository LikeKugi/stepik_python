number = int(input())

if number > 0:
    print('positive')
elif number == 0:
    print('0')
else:
    print('negative')
# //////////////////////////////////
number = int(input())
print(10 <= number <= 100)  # number >= 10 and number <= 100
# //////////////////////////////////
x1, x2, x3 = False, True, False
print(not x1 or x2 and x3)
print((not x1 or x2) and x3)