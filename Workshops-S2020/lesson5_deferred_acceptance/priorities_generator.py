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
