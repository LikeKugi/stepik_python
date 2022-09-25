speed_zoom, speed_flash = int(input()), int(input())
if speed_zoom > speed_flash:
    print('NO')
elif speed_zoom < speed_flash:
    print('YES')
else:
    print("Don't know")