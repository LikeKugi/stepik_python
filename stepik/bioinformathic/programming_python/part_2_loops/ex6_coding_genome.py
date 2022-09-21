genome = input()
output = ''
counter = 0
current_char = genome[0]
for i in range(len(genome)):
    if genome[i] == current_char:
        counter += 1
    else:
        output += current_char + str(counter)
        counter = 1
        current_char = genome[i]
output += current_char + str(counter)
print(output)
