color1, color2 = input(), input()
if color1 not in ['красный', 'синий', 'желтый'] or color2 not in ['красный', 'синий', 'желтый']:
    print('ошибка цвета')
elif color1 == color2:
    print(color1)
elif color1 in ('красный', 'синий') and color2 in ('красный', 'синий'):
    print('фиолетовый')
elif color1 in ('красный', 'желтый') and color2 in ('красный', 'желтый'):
    print('оранжевый')
else:
    print('зеленый')
