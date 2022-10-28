# Ваша задача создать функцию make_header, которая принимает
#
# обязательный параметр - строку, которую нужно обернуть в тег заголовка
# необязательный числовой параметр - уровень заголовка, по умолчанию принимает значение 1.
# Функция make_header должна возвращать переданную строку в обернутый тег заголовка определенного уровня

def make_header(header: str, title: int = 1) -> str:
   return f'<h{title}>{header}</h{title}>'


print(make_header('Нет'))
print(make_header('Bella Ciao', 4))
print(make_header('Go little rock star', 6))
print(make_header('Девальвации не будет. Твердо и четко'))