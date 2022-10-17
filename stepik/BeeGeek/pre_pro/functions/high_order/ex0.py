def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']

words_len = map(len, words)
print(max(words_len))


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result


def predicate(word):
    return word == word[::-1]


words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister',
         'surface', '1234321']
filtered = filter(predicate, words)
print(len(filtered))


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

var1 = max(numbers, key=abs)
var2 = min(map(abs, numbers))

print(var1 + var2)
