def fancy(length, char1, char2):
    return (char1 + char2) * length + char1


print(fancy(5, '-', '*'))


def fancy1(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy1(3))


def fancy2(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy2(3, '.'))


def fancy4(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy4(2, ':', '|'))


def fancy5(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy5(4, char2='#'))


def fancy6(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


print(fancy6(char2='$', length=3))

def fancy7(length, char1='-', char2='*'):
    return (char1 + char2) * length + char1


#print(fancy7(char2='!'))
