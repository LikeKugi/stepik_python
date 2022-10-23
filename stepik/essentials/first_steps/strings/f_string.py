x = 11
y = 98
print(f"{x=}, {y=}")
#пробелы будут учтены
print(f"{x  =}, {y= }")

a = 1/8
b = 1/2
c = 1/3
print(f'{a = :.3f}')
print(f'{b = :.3f}')
print(f'{c = :.3f}')
print('------')
print(f'{c:.3f}')
print(f'{c:.1f}')
print(f'{c:.2f}')
print(f'{c:.10f}')

d = 100
print(f'{d:.1f}')
print(f'{d:.2f}')
print(f'{d:.3f}')

n = 12345
print(f'{n:8d}')
print(f'{n:7d}')
print(f'{n:6d}')
print(f'{n:5d}')
print(f'{n:4d}')

n = 12345
print(f'{n:08d}')
print(f'{n:07d}')
print(f'{n:06d}')
print(f'{n:05d}')
print(f'{n:04d}')

n = 12345678912345

print(f'{n:,d}')
print(f'{n:_d}')

sep = '_'
print(f'{n:{sep}d}') # вложенная f-строка

print(f'Число\t\tКвадрат\t\tКуб')
for x in range(1, 11):
   print(f'{x:2d}\t\t{x*x:3d}\t\t{x*x*x:4d}')