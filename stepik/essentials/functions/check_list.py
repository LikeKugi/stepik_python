#  Ваша задача написать функция find_duplicate, которая принимает один аргумент - список чисел.
#  Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке,
#  в котором они встречаются в исходном списке. Под дублем будем подразумевать число, которое присутствовало
#  в списке несколько раз.


def find_duplicate(lst: list) -> list:
    used = set()
    out = []
    for number in lst:
        if number not in used and lst.count(number) > 1:
            out.append(number)
        used.add(number)
    return out


for x in [[1, 1, 1, 1, 1, 2, 2, 2, 2], [2, 1, 1, 1, 1, 1, 2, 2, 2, 2], [1, 2, 3, 4], [1, 2, 3, 4, 3]]:
    print(find_duplicate(x))
