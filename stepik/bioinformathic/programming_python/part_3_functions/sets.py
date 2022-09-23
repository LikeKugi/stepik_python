s = set()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
for x in basket:
    print(x)
print('orange' in basket)
print('python' in basket)
s.add('element')
print(s)
s.remove('element')
s.discard('red')
s.clear()
print(s)