n = int(input())
stack = []
maximums = []


for _ in range(n):
    query = input()
    match query:
        case 'pop':
            stack.pop()
            maximums.pop()
        case 'max':
            print(maximums[-1] if maximums else 0)
        case _:
            _, num = query.split(' ')
            num = int(num)
            if (not stack) or (num >= (m := maximums[-1])):
                stack.append(num)
                maximums.append(num)
            else:
                stack.append(num)
                maximums.append(m)



