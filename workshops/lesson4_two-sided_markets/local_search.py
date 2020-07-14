from stability_check import is_stable
from priorities_generator import generate_priorities

# функция для добавления новой пары в распределение
def change_matching(matching, pair):
    man = pair[0]
    woman = pair[1]

    # находим, с кем в паре состояли люди из новой пары
    for i in range(len(matching)):
        if man in matching[i]:
            man_matching_n = i
            man_matching = matching[i][1]
        if woman in matching[i]:
            woman_matching_n = i
            woman_matching = matching[i][0]

    # удаляем пары, в которых состояли люди из новой пары
    matching = matching[:man_matching_n] + matching[man_matching_n + 1:]
    if man_matching_n < woman_matching_n:
        matching = matching[:woman_matching_n - 1] + matching[woman_matching_n:]
    else:
        matching = matching[:woman_matching_n] + matching[woman_matching_n + 1:]

    # добавляем новую пару и пару, составленную из "брошенных" людей
    matching.append(pair)
    matching.append([woman_matching, man_matching])

    return matching


def local_search(priorities, matching):
    """
    Функция для поиска стабильного распределения в задаче марьяжа методов локального
    поиска

    priorities: приоритеты сторон
    matching: начальное распределение
    """
    blocking_pairs = is_stable(priorities, matching)[1]

    while blocking_pairs != []:

        pair_new_matching = change_matching(matching, blocking_pairs[0])
        pair_new_blocking = is_stable(priorities, pair_new_matching)[1]
        min_blocking = len(pair_new_blocking)
        min_matching = pair_new_matching

        # для каждой пары проверяем, сколько будем блокирующих пар после её смены
        # выбираем ту, после которой появится меньше всего блокирующих пар
        for i in range(1, len(blocking_pairs)):
            pair_new_matching = change_matching(matching, blocking_pairs[i])
            pair_new_blocking = is_stable(priorities, pair_new_matching)[1]

            if len(pair_new_blocking) <= min_blocking:
                min_blocking = len(pair_new_blocking)
                min_matching = pair_new_matching

        matching = min_matching
        blocking_pairs = is_stable(priorities, matching)[1]

    return matching

priorities = generate_priorities(5, 5, 1)

for pr in priorities:
    for person in pr:
        print(person, pr[person])
    print()

matching = [['m1','w1'], ['m2','w2'], ['m3','w3'], ['m4','w4'], ['m5','w5']]
print(local_search(priorities, matching))
