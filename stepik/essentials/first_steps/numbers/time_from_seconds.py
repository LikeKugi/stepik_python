"""
Электронные часы показывают время в формате h:mm:ss,
то есть сначала записывается количество часов в диапазоне от 0 до 23,
потом обязательно двузначное количество минут,
затем обязательно двузначное количество секунд.
Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

Программа получает на вход число n - количество секунд, которое прошло с начала суток.

Выведите показания часов, соблюдая формат.
"""
seconds = int(input())
hh = seconds // 3600 % 24
mm = (seconds % 3600) // 60
ss = seconds % 3600 % 60
print(f'{hh}:{mm:02}:{ss:02}')

