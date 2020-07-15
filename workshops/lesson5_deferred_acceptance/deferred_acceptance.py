from priorities_generator import generate_priorities
from stability_check import blocking_pairs

def reverse_dict(d):
    """
    Функция меняет местами ключи и значения в словаре с сохранением всех ключей,
    которые указывали на одно и то же значение

    Пример: {a: 1, b: 2, c: 1} -> {1: [a, c], 2: [b]}
    """

    dinv = {}
    for k, v in d.items():
        if v in dinv:
            dinv[v].append(k)
        else:
            dinv[v] = [k]
    return dinv

def choose_best(priorities, offers):
    """
    Функция для выбора среди всех предложений то, которое стоит выше в списке
    приоритетов

    priorities: приоритеты получающих предложения
    offers: предложения второй стороны
    """

    offers = reverse_dict(offers)
    choice = {}

    for woman in priorities:
        if woman in offers:
            choice[woman] = min(offers[woman],
                                key=lambda man: priorities[woman]['priorities'].index(man))

    return choice

def deferred_acceptance(priorities):
    """
    Функция для нахождения стабильного распределения для задачи марьяжа

    priorities: предпочтения сторон
    """
    # начальное задание шортлистов
    men_priorities = priorities[0]
    women_priorities = priorities[1]

    men_choice = {}
    women_choice = {}

    # пока у всех женщин не будет партнеров
    while len(women_choice) != len(women_priorities):
        # мужчины выбирают первую женщину в списке приоритетов
        men_choice = {man: men_priorities[man]['priorities'][0] for man in men_priorities}
        # женщины выбирают среди предложений самое лучшее
        women_choice = choose_best(women_priorities, men_choice)

        # для каждой женщины, которой поступило предложение
        for woman in women_choice:
            woman_pr = women_priorities[woman]['priorities']
            # для каждого мужчины хуже тех, кого выбрала женщина
            for man in woman_pr[woman_pr.index(women_choice[woman])+1:]:
                man_pr = men_priorities[man]['priorities']
                # удаляем женщину, которая в любом случае не выберет этого мужчину
                del man_pr[man_pr.index(woman)]
                # удаляем мужчину, с которым женщина в любом случае не согласится
                # вступить в брак
                del woman_pr[woman_pr.index(man)]

    # формируем распределение
    matching = [[k,v] for k,v in men_choice.items()]
    return matching, (men_priorities, women_priorities)

if __name__ == '__main__':
    priorities = generate_priorities(5, 5, 1)
    
    print('Предпочтения:')
    for pr in priorities:
        for person in pr:
            print(person, pr[person])
        print()

    matching, shortlist = deferred_acceptance(priorities)
    print('Распределение:')
    print(matching)
    print('Шортлисты:')
    for pr in shortlist:
        for person in pr:
            print(person, pr[person])
        print()

    not_acceptable, bl_pairs = blocking_pairs(priorities, matching)
    print("Неприемлемые пары:", not_acceptable)
    print("Блокирующие пары:", bl_pairs)
