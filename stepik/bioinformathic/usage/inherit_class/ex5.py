import sys

TEST_FLAG = False

if TEST_FLAG:
    sys.stdin = open('input_1.txt', 'r')
    # sys.stdout = open('out_1.txt','a')

classes = {}


def is_inherit(pr, inh):
    if pr == inh or pr in classes.get(inh):
        return True
    if not classes.get(inh):
        return False
    else:
        for el in classes.get(inh):
            if is_inherit(pr, el):
                return True
    return False


for _ in range(int(input())):
    line = input()
    if ':' in line:
        key, inherit = line.split(' : ')
        classes.setdefault(key, []).extend(inherit.split())
    else:
        classes[line] = []

print(classes)

if TEST_FLAG:
    with open('out_1.txt') as inf:
        data = inf.readlines()
        for i in range(int(input())):
            parent, inherit = input().split()
            print(f'{parent} : {inherit}')
            if is_inherit(parent, inherit) and data[i].rstrip() == 'Yes':
                print('good')
            elif not is_inherit(parent, inherit) and data[i].rstrip() == 'No':
                print('good')
            else:
                print('nooo')
            print(('No', 'Yes')[is_inherit(parent, inherit)])
else:
    for i in range(int(input())):
        parent, inherit = input().split()
        print(f'{parent} : {inherit}')

        print(('No', 'Yes')[is_inherit(parent, inherit)])
