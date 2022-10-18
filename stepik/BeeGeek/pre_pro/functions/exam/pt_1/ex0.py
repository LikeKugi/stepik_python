def add_five(a, b):
    return a+5, b+5

result = add_five(3, 2)
print(result)

def func(a,b,c,d):
    pass

func(a=1, b=2, c=3, d=4)
func(1, 2, 3, d=4)
#func(a=1, b=2, c=3, 4)
func(1, 2, 3, 4)
#func(a=1, 2, 3, 4)

def func(name, age=20):
    print(name, age)

func('Emma', 25)

def func(name, age):
    print(name, age)

#func(name='Timur', 28)
#func(age=28, 'Timur')
func(age=28, name='Timur')