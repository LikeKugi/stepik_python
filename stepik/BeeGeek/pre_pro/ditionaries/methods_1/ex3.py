"""
Дополните приведенный код так, чтобы в переменной result хранился словарь,
в котором для каждого символа строки text будет подсчитано количество его вхождений.
"""

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

text_chars = set(text)
result = {}
for char in text_chars:
    result[char] = text.count(char)
print(result)


result = {char: text.count(char) for char in set(text)}
print(result)