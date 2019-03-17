movies = {"Пятница": {'12': 250, '16': 350, '20': 450},
          "Чемпионы": {'10': 250, '13': 350, '16': 350},
          "Пернатая банда": {'10': 350, '14': 450, '18': 450}}

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
time = input("Выберите время: ")
tickets = input("Выберите количество билетов: ")

if movie and day and time and tickets:
    tickets = int(tickets)
    if movie in movies:
        if day == "сегодня" or day == "завтра":
            if time in movies[movie]:
                print("Фильм:", movie, "День:", day, "Время:", time, "Количество билетов:", tickets)
                print("Итого:", price(movies[movie], tickets, day, time))
            else:
                print("На это время нет сеансов, попробуйте еще раз")
        else:
            print("Неправильно указан день, попробуйте еще раз")
    else:
        print("Такого фильма нет, попробуйте еще раз")
else:
    print("Некоторые параметры не указаны, попробуйте еще раз")
            
