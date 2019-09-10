import json 

def writer(filename, numbers):
    '''
    Запись в json файл 
    '''   
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as e:
        print(e)

def reader(filename):
    '''
    Чтение содержимого json файла 
    '''   
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as e:
        return e

todoList = list(reader('tasks.json'))
while True:
    try:
        number = int(input(
        'Простой todo:\n\t1. Добавить задачу.\n\t2. Удалить задачу.\n\t3. Вывести список задач.\n\t4. Выход.\nУкажите число: '))    
        if number == 4:
            break
        elif number == 3:
            count = 0
            for task in todoList:
                count += 1
                print(str(count)+" задача")
                for name in task:
                    print('\t'+name+':', task[name])
                print()
        elif number == 2:
            taskNum = int(input("Введите номер задачи: "))-1
            task = todoList[taskNum]
            print("Вы хотите удалить эту задачу?")
            for name in task :
                    print('\t'+name+':', task[name])
            answer = input("Да/Нет: ")
            if answer.lower() == "да":
                todoList.remove(task)
                writer('tasks.json', todoList)
                print("Задача успешно удалена")
            elif answer.lower() == "нет":
                print("Вы решили ничего не удалять")
            else:
                raise ValueError               
        elif number == 1:
            newTask = {}
            newTask['Задача'] = input('Сформулируйте задачу: ')
            newTask['Категория'] = input('Добавьте категорию к задаче: ')
            newTask['Время'] = input('Добавьте время к задаче: ')
            todoList.append(newTask)
            writer('tasks.json', todoList)
        else:
            raise ValueError
    except IndexError:
        print("Такой задачи нет, проверьте номер требуемой задачи")
    except ValueError:
        print("Ошибка ввода, попробуйте еще раз")
