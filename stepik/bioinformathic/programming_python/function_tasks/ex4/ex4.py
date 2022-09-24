coords = [0, 0]


def move_forward(coords, move):
    coords[1] += move


def move_side(coords, move):
    coords[0] += move


for _ in range(int(input())):
    direction, move = input().split()
    move = int(move)
    if direction == 'юг' or direction == 'запад':
        move *= -1
    print(direction, move)
    if direction == 'север' or direction == 'юг':
        move_forward(coords, move)
    else:
        move_side(coords, move)
print(*coords)
