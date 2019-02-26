number = int(input("Введите номер элемента: "))
if number:
    if number == 3:
        print("Литий")
    elif number == 12:
        print("Магний")
    elif number == 80:
        print("Ртуть")
    elif number == 17:
        print("Хлор")
    else:
        print("Что это?")
else:
    print("Введите номер элемента!")
