namespaces = {
    'global': {
        'var': [],
        'parent': None
    }
}

for _ in range(int(input())):
    operation, namespace, define = input().split()
    if operation == 'add':
        namespaces[namespace]['var'].append(define)
    elif operation == 'create':
        namespaces[define]['var'].append(namespace)
        namespaces[namespace] = {'var': [],'parent': define}
    elif operation == 'get':
        if define in namespaces.get(namespace)['var']:
            print(namespace)
        else:
            look = namespaces.get(namespace)['parent']
            while look:
                print(f'{define} looking in - {look}')
                if define in namespaces.get(look)['var'] :
                    print(look)
                    break
                look = namespaces.get(look)['parent']
            else:
                print(None)

print(namespaces)