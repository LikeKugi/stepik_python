# На вход программе подается строка текста, содержащая числа.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности
# или NO, если не встречалось.

numbers = [int(number) for number in input().split()]
unique = set()
for number in numbers:
    if number not in unique:
        unique.add(number)
        print('NO')
    else:
        print('YES')