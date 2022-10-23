# <  Выравнивает выражение в фигурных скобках по левому краю. У строк такое поведение по умолчанию
# >  Выравнивает выражение в фигурных скобках по правому краю. У чисел такое поведение по умолчанию
# ^  Выравнивает выражение в фигурных скобках по центру

number = 12345.6789
print(f"Число {number = }")
print(f"|{number:25}|")
print(f"|{number:<25}|")
print(f"|{number:>25}|")
print(f"|{number:^25}|")
print('-'*25)
text = "Python 3.10"
print(f"Строка {text = }")
print(f"|{text:25}|")
print(f"|{text:<25}|")
print(f"|{text:>25}|")
print(f"|{text:^25}|")

number = 12345.6789
print(f"Число {number = }")
print(f"|{number:=<25}|")
print(f"|{number:=>25}|")
print(f"|{number:=^25}|")
print('-'*25)
text = "Python 3.10"
print(f"Строка {text = }")
print(f"|{text:-<25}|")
print(f"|{text:!>25}|")
print(f"|{text:?^25}|")