def cycle_list(list):
    pos_max = list.index(max(list))
    pos_min = list.index(min(list))
    diff = pos_min - pos_max
    shift = list[diff:] + list[:diff]
    return shift

list = [int(item) for item in input("Введите список чисел:\n").split()]
print(cycle_list(list))
