import random

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)

print(num1)
print(num2)

for _ in range(10):
    print(random.randint(1, 100))

num = random.randrange(10)
print(num)
num = random.randrange(5, 10)
print(num)
num = random.randrange(0, 101, 10)
print(num)
num = random.random()
print(num)
num = random.uniform(1.5, 17.3)
print(num)

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100),end=' ')
print()
