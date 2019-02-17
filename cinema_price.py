friday = {12: 250, 16: 350, 20: 450}
champions = {10: 250, 13: 350, 16: 350}
gang = {10: 350, 14: 450, 18: 450}

def day_discount(day):
    if day == "сегодня":
        return 0
    elif day == "завтра":
        return 0.05

def tickets_discount(tickets):
    if tickets < 20:
        return 0
    else:
        return 0.20

def price(movie, tickets, day, time):
    return tickets*movie[time] - tickets*movie[time]*(day_discount(day) + tickets_discount(tickets))

movie = input("Выберите фильм: ")
day = input("Выберите день (сегодня, завтра): ")
time = int(input("Выберите время: "))
tickets = int(input("Выберите количество билетов: "))

if movie and day and time and tickets:
    if day == "сегодня" or "завтра":
        if movie == "Пятница":
            if time in friday:
                print("Фильм: Пятница", "День:", day, "Время:", time, "Количество билетов:", tickets)
                print("Итого:", price(friday, tickets, day, time))
            else:
                print("На это время нет сеансов, попробуйте еще раз")
        elif movie == "Чемпионы":
            if time in champions:
                print("Фильм: Чемпионы", "День:", day, "Время:", time, "Количество билетов:", tickets)
                print("Итого:", price(champions, tickets, day, time))
            else:
                print("На это время нет сеансов, попробуйте еще раз")
        elif movie == "Пернатая банда":
            if time in gang:
                print("Фильм: Пернатая банда", "День:", day, "Время:", time, "Количество билетов:", tickets)
                print("Итого:", price(gang, tickets, day, time))
            else:
                print("На это время нет сеансов, попробуйте еще раз")
        else:
            print("Такого фильма нет, попробуйте еще раз")
    else:
        print("Неправильно указан день, попробуйте еще раз")
else:
    print("Один из параметров не выбран или выбран неправильно, попробуйте еще раз")
