"""
Хороший пароль по условиям этой задачи состоит как минимум из 77 символов, содержит хотя бы одну цифру,
заглавную и строчную букву. Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.
"""

password = input()
print(('NO','YES')
      [int(all([
                any([el.isdigit() for el in password]),
                any([el.islower() for el in password]),
                any([el.isupper() for el in password]),
                len(password)>6
                ]))
      ]
      )