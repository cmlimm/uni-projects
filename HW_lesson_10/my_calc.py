def result(first, second, operator):
    if operator == "+":
        return first+second
    if operator == "-":
        return first - second
    if operator == "*":
        return first*second
    if operator == "/":
        return first/second
    else:
        raise ValueError("Could not convert string to operator: "+"'"+operator+"'")

while True:
    try:
        print('Для выхода введите в любое поле "Выход"')
        firstNum = float(input("Введите первое число: "))
        secondNum = float(input("Введите второе число: "))
        operator = input("Введите оператор: ")
        print("Результат:", result(firstNum, secondNum, operator))
    except ValueError as err:
        if str(err).split()[-1].lower() == "'выход'":
            break
        print("Ошибка ввода, попробуйте еще раз")
    except ZeroDivisionError:
        print("Ошибка деления на ноль, попробуйте еще раз")
