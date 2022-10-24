lang = input("Какой язык программирования будем учить?")

match lang:
    case "JavaScript":
        print("Ты можешь стать фронтенд разработчиком")
    case "Python":
        print("Ты можешь стать Data Scientist-ом")

    case "PHP":
        print("Ты можешь стать бекенд разработчиком")

    case "Solidity":
        print("Ты можешь стать Blockchain разработчиком")

    case "Java":
        print("Ты можешь стать мобильным разработчиком")
    case  _:
        print("Язык не важен, главное уметь решать задачи)")


# Сравнение на несколько значений

digit = int(input("Введите цифру: "))

match digit:
    case 0 | 3 | 6 | 9:
        print("Без остатка делятся на 3")
    case 1 | 4 | 7:
        print("При делении на 3 дают остаток 1")
    case 2 | 5 | 8:
        print("При делении на 3 дают остаток 2")
    case  _:
        print(f"{digit} не является цифрой")