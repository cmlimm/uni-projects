todoList = []
while True:
    number = int(input(
        'Простой todo:\n\t1. Добавить задачу.\n\t2. Вывести список задач.\n\t3. Выход.\nУкажите число: '))    
    if number == 3:
        break
    if number == 2:
        for task in todoList:
            for name in task:
                print(name+':', task[name])
            print()
    if number == 1:
        newTask = {}
        newTask['Задача'] = input('Сформулируйте задачу: ')
        newTask['Категория'] = input('Добавьте категорию к задаче: ')
        newTask['Время'] = input('Добавьте время к задаче: ')
        todoList.append(newTask)
