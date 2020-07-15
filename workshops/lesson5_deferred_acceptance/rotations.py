from deferred_acceptance import deferred_acceptance, reverse_dict
from priorities_generator import generate_priorities
from stability_check import blocking_pairs

# возвращает True если list1 пересекается с list2
def intersecting(list1, list2):
    return any(x in list2 for x in list1)

def rotations(shortlists, matching):

    # шортлисты мужчин
    men_shortlists = shortlists[0]
    # перевод распределения из вида м: ж в вид ж: м
    reverse_matching = {v: k for k, v in matching.items()}

    # список всех мужчин
    men = list(men_shortlists.keys())
    cycles = []
    for man in men:
        current_man = man
        cur_priorities = men_shortlists[current_man]['priorities']
        cycle = []
        # пока не дойдем до мужчины, что уже есть в цикле
        while current_man not in cycle:
            # если у мужчины нет потенциальной пары с меньшим приоритетом, то
            # цикла не существует
            if cur_priorities.index(matching[current_man]) == len(cur_priorities) - 1:
                cycle = []
                break

            cycle.append(current_man)
            # рассматриваем следующий приоритет мужчины
            second_woman = cur_priorities[1]
            # находим мужчину, с кем в паре женщина, найденная ранее
            current_man = reverse_matching[second_woman]
            cur_priorities = men_shortlists[current_man]['priorities']

        if cycle != []:
            cycles.append(cycle)

    true_cycles = []
    # для каждого необработанного цикла
    for cycle in cycles:
        # если цикл не пересекается ни с одним "настоящим" циклом, то добавляем
        # его в настоящие
        if all(not intersecting(cycle, true_cycle) for true_cycle in true_cycles):
            true_cycles.append(cycle)
        else:
            # если цикл пересекается с каким-то "настоящим" циклом, то
            # для каждого "настоящего" цикла проверяем, является ли
            # текущий цикл его подмножеством меньшего размера
            # если да, то заменяем "настоящий" цикл на этот
            for c in true_cycles:
                if intersecting(cycle, c) and len(cycle) < len(c) and len(cycle) != 1:
                    del true_cycles[true_cycles.index(c)]
                    true_cycles.append(cycle)
                    break

    # делаем список ротаций по циклам
    rotation_list = []
    for cycle in true_cycles:
        rotation_list.append([])
        for man in cycle:
            rotation_list[-1].append([man, matching[man]])

    return rotation_list

def perform_rotation(rotation, matching):
    men = [pair[0] for pair in rotation]
    women = [pair[1] for pair in rotation]

    women = women[1:]+[women[0]]
    for man, woman in zip(men, women):
        matching[man] = woman

    return matching

def all_stable_matchings(shortlists, matching):

    men_shortlists = shortlists[0]
    women_shortlists = shortlists[1]
    matching = {pair[0]: pair[1] for pair in matching}
    matchings = [matching.copy()]
    rots = rotations(shortlists, matching)

    # while rots != []:
    #     submatching = matching
    #     for rot in rots:
    #         matchings.append(perform_rotation(rot, submatching))
    #         matching = perform_rotation(rot, matching)
    #     if len(rots) != 1:
    #         matchings.append(matching)
    #     rots = rotations(shortlists, matching)

    return rots

if __name__ == '__main__':
    priorities = generate_priorities(5, 5, 1)
    print('Предпочтения:')
    for pr in priorities:
        for person in pr:
            print(person, pr[person])
        print()

    matching, shortlists = deferred_acceptance(priorities[::-1])
    print('Распределение:')
    print(matching)
    print('Шортлисты:')
    for pr in shortlists:
        for person in pr:
            print(person, pr[person])
        print()

    matching, shortlists = deferred_acceptance(priorities)
    print('Распределение:')
    print(matching)
    print('Шортлисты:')
    for pr in shortlists:
        for person in pr:
            print(person, pr[person])
        print()

    not_acceptable, bl_pairs = blocking_pairs(priorities, matching)
    print("Неприемлемые пары:", not_acceptable)
    print("Блокирующие пары:", bl_pairs)
    for matching in all_stable_matchings(shortlists, matching):
        print(matching)
