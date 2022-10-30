#  Введите с клавиатуры список с различными значениями (цифры, слова, символы).
#  Необходимо проверить, есть ли в этом списке два слова подряд и вывести их на экран.
#  Если таких пар нет, то выведите фразу “Мало слов!”.

def solution():
    x = input().split()
    flag = False
    for i in range(len(x)-1):
        if x[i].isalpha() and x[i+1].isalpha():
            print(x[i],x[i+1])
            flag = True
    if not flag:
        print('Мало слов!')

solution()