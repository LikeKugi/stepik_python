# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

# Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a.
# Если операций потребуется более 1000, выведите Impossible.
#
# Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
# или Impossible, если операций потребуется более 1000.

def replacing(s: str, a: str, b: str):
    if a in s and a == b:
        return 'impossible'
    counter = 0
    while a in s or counter > 1000:
        counter += 1
        s = s.replace(a, b)
    return counter if counter <= 1000 else 'impossible'


print(replacing('ababa', 'a', 'b'))
print(replacing('ababa', 'b', 'a'))
print(replacing('ababa', 'c', 'c'))
print(replacing('ababac', 'c', 'c'))
