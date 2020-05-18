numberSum = 0
while True:
    number = input("Введите число или Стоп для выхода: ")
    if not number.isdigit():
        if number.lower() == "стоп":
            print("Сумма:", numberSum)
            break
        else:
            print("Ошибка ввода.")
    else:
        numberSum += int(number)
