with open('words.txt', encoding='utf-8') as file:
    line1 = file.readline().split()
    file.seek(0)
    line2 = file.readline().split()

    print(max(line2, key=len))