with open('words.txt', 'w') as output:
    print('stepik', 'beegeek', 'iq-option', sep='*', end='+\n', file=output)
    print('python', file=output)

with open('beegeek.txt', 'w') as file:
    file.writelines(['Добро пожаловать в Beegeek!\n', 'Наши курсы самые лучшие! '])
    file.write('Позвоните нам: (916) 928-92xx')