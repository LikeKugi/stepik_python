# Иногда некоторые слова вроде «civilization» или «internationalization» настолько длинны,
# что их весьма утомительно писать много раз в каком либо тексте.
#
# Будем считать слово слишком длинным, если его длина строго больше 10 символов.
# Все слишком длинные слова можно заменить специальной аббревиатурой.
#
# Эта аббревиатура строится следующим образом: записывается первая и последняя буква слова,
# а между ними — количество букв между первой и последней буквой (в десятичной системе счисления и без ведущих нулей).
#
# Таком образом, «civilization» запишется как «c10n», а «internationalization» как «i18n».
#
# Вам предлагается автоматизировать процесс замены слов на аббревиатуры.
# При этом все слишком длинные слова должны быть заменены аббревиатурой, а слова, не являющиеся слишком длинными,
# должны остаться без изменений.

words = list(
    word if len(word := input()) <= 10 else str(word[0] + str(len(word[1:-1])) + word[-1]) for _ in range(int(input())))

print(*words, sep='\n')