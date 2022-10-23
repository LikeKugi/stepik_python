name = 'Семён'
mid_name = 'Семёнов'
balance = 32.56

text = """Дорогой {0} {1}, 
баланс Вашего лицевого счёта составляет {2} руб.""".format(mid_name, name, balance)

print(text)

text = """Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {balance} руб.""".format(mid_name=mid_name, name=name, balance=balance)

print(text)

text = """Дорогой {name} {mid_name}, 
баланс Вашего лицевого счёта составляет {balance} руб. {name}""".format(mid_name=mid_name, name=name, balance=balance)

print(text)

