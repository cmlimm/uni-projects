def price(city, time):
    if city == 343:
        return time*15
    elif city == 381:
        return time*18
    elif city == 473:
        return time*13
    elif city == 485:
        return time*11

city = int(input("Введите код города: "))
time = int(input("Введите длительность звонка в минутах: "))
print("Стоимость звонка:", price(city, time), "рублей")
