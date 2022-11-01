exceptions = {}
stack = set()


def create_exceptions(exc: dict) -> dict:
    for _ in range(int(input())):
        line = input()
        parents = None
        if ':' in line:
            exception, parents = line.split(' : ')
        else:
            exception = line

        exc[exception] = {'inerhit': set(), 'parent': []}
        if parents:

            if isinstance(parents.split(), str):
                exc[exception]['parent'].append(parents)
                # exc[exception]['parent'].extend(exc[parents]['parent'])
                #exc[parents]['inerhit'].append(exception)
            else:
                # for el in parents.split():
                #     exc.setdefault(el, {'inerhit': [], 'parent': []})
                exc[exception]['parent'].extend(parents.split())
                    # exc[exception]['parent'].extend(exc[el]['parent'])
                    #exc[el]['inerhit'].append(exception)
    return exc


def searching_parents():
    for key in exceptions:
        for el in exceptions[key]['parent']:
            exceptions[el]['inerhit'].add(key)
            exceptions[el]['inerhit'].update(exceptions[key]['inerhit'])


def create_queries():
    for _ in range(int(input())):
        #print(stack)
        exception = input()
        if exception in stack:
            print(exception)
        stack.add(exception)
        stack.update(exceptions[exception]['inerhit'])


def main():
    create_exceptions(exceptions)
    #print(exceptions)
    searching_parents()
    #print(exceptions)
    create_queries()


if __name__ == '__main__':
    #for i in range(4,5):
        #sys.stdout = open(f'output_{i}.txt', 'w')
        exceptions.clear()
        stack.clear()
        #print(f'input_{i}.txt')
        #sys.stdin = open(f'input_{i}.txt', 'r')
        main()