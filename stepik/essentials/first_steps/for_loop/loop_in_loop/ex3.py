cells = [[el for el in input()] for _ in range(4)]
flag = True
for i in range(3):
    for j in range(3):
        if len({cells[i][j], cells[i + 1][j], cells[i][j + 1], cells[i + 1][j + 1]}) == 1:
            flag = False
            break
    if not flag:
        break
print(('No','Yes')[flag])