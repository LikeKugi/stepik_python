def f(x, y):
    result = None

    try:
        result = x / y

    except (TypeError, ZeroDivisionError) as e_name:
        print('error in function')
        print(e_name.args)

    except Exception as e_other:
        print('error')
        print(e_other)

    else:                   # if no exceptions
        print('try done')

    finally:                # anyway
        print('finaly')
        return result


print(f(5, []))
try:
    print(f(5, 0))
except ZeroDivisionError:
    print('not in f but err')

print(ZeroDivisionError.mro())  # наследие ошибок
