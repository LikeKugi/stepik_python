tpl = (10, 20, 30, 40, 50, 60, 70, 80)
print(tpl[2:5], tpl[:4], tpl[3:])
print()

tpl = (100, 200, 300, 400, 500)
print(tpl[-2])
print(tpl[-4:-1])
print()

tpl = (1777, 'a')
#print(max(tpl))
print()

tpl = (100, 200, 300, 400, 500)
#tpl[1] = 700
print(tpl)
print()

tpl = ('Green')
print(type(tpl))
tpl = ('Green',)
print(type(tpl))
print()

tpl = (100, 200, 300, 400, 500)
#tpl.pop(2)
print(tpl)
print()

a, *b, c = 'No bees', 'no honey'
print(b)