from random import sample

def generate_priorities(men_n, women_n, quota):
    """
    Функция генерирует списки предпочтений для задачи марьяжа в следующем виде:
    {игрок: {'priorities': предпочтения, 'quota': квота}, ...}

    men_n: количество  мужчин
    women_n: количество женщин
    quota: квота
    """

    men_list = ['m'+str(i) for i in range(1, men_n + 1)]
    women_list = ['w'+str(i) for i in range(1, women_n + 1)]

    men_priorities = {man: {'priorities': sample(women_list, women_n),
                            'quota': quota} for man in men_list}
    women_priorities = {woman: {'priorities': sample(men_list, men_n),
                                'quota': quota} for woman in women_list}

    return (men_priorities, women_priorities)

# функция для проверки приемлемости пары
def is_acceptable(priorities, pair):
    man = pair[0]
    woman = pair[1]

    if woman not in priorities[0][man]['priorities']:
        return False

    if man not in priorities[1][woman]['priorities']:
        return False

    return True

# функция проверяет, является ли пара блокирующей
def is_blocking(priorities, matching, pair):
    man = pair[0]
    woman = pair[1]

    man_priorities = priorities[0][man]['priorities']
    woman_priorities = priorities[1][woman]['priorities']

    for pair in matching:
        if man in pair:
            man_matching = pair[1]
        if woman in pair:
            woman_matching = pair[0]

    if man_priorities.index(man_matching) > man_priorities.index(woman) and \
       woman_priorities.index(woman_matching) > woman_priorities.index(man):
        return True

    return False

def is_stable(priorities, matching):
    """
    Функция для проверки стабильности распределения

    priorities: предпочтения сторон
    matching: распределение
    """

    men_list = [man for man in priorities[0]]
    women_list = [woman for woman in priorities[1]]

    not_acceptable = []
    blocking = []

    # проверяем наличие неприемлемых пар
    for pair in matching:
        if not is_acceptable(priorities, pair):
            not_acceptable.append(pair)

    # проверяем наличие блокирующих пар
    for man in men_list:
        for woman in women_list:
            if [man, woman] not in matching:
                if is_acceptable(priorities, [man, woman]):
                    if is_blocking(priorities, matching, [man, woman]):
                        blocking.append([man, woman])

    return (not_acceptable, blocking)

priorities = generate_priorities(5, 5, 1)

for pr in priorities:
    for person in pr:
        print(person, pr[person])
    print()

matching = [['m1','w1'], ['m2','w2'], ['m3','w3'], ['m4','w4'], ['m5','w5']]
stable_check = is_stable(priorities, matching)
print("Неприемлемые пары:", stable_check[0])
print("Блокирующие пары:", stable_check[1])
