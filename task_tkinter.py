# -*- coding: utf8 -*-
import tkinter
import json 

def writer(filename, numbers):
    '''
    Запись в json файл 
    '''   
    try:
        with open(filename, 'w') as f_obj:
            json.dump(numbers, f_obj)
    except Exception as err:
        error(err)

def reader(filename):
    '''
    Чтение содержимого json файла 
    '''   
    try:
        with open(filename) as f_obj:
            numbers = json.load(f_obj)
        return numbers
    except Exception as err:
        error(err)

def error(err):
    """
    Окно с уведомлением об ошибке
    """
    error_window = tkinter.Toplevel()
    error_window.title("Ошибка")
    error_window.geometry('+420+250')
    error_text = tkinter.StringVar()
    error_text.set(err)
    error_message = tkinter.Label(error_window,
                                  textvariable=error_text)
    error_message.grid(row=0, column=0)
    button_ok = tkinter.Button(error_window,
                             text='Ок',
                             command=error_window.destroy)
    button_ok.grid(row=1, column=0)
    error_window.mainloop()
    
def add_task():
    """
    Добавление задания
    """
    try:
        newTask = {}
        newTask['Задача'] = task.get()
        newTask['Категория'] = cat.get()
        newTask['Время'] = time.get()
        todoList.append(newTask)
        writer('tasks.json', todoList)
        task.set('')
        cat.set('')
        time.set('')
        info.set('Задача добавлена')
        announcer.after(2000, lambda: info.set(''))
        show_task()
    except Exception as err:
        error(err)
    
def delete_task():
    """
    Окно удаления задания
    """
    try:
        delete_window = tkinter.Toplevel()
        delete_window.title("Удаление задачи")
        delete_window.geometry('+400+225')
        
        question = tkinter.Label(delete_window,
                                 text="Выберите задачу")
        question.grid(row=0, column=0)
        
        show_delete = tkinter.Label(delete_window, text='')
        show_delete.grid(row=3, column=0)
        
        def show_one_task():
            """
            Вывод удаляемого задания
            """
            try:
                temp_task = ''
                for name in todoList[int(task_n.get())-1]:
                    temp_task = temp_task + name + ': ' + todoList[int(task_n.get())-1][name] + '\n'
                show_delete.configure(text=temp_task)
                show_delete.update_idletasks()
            except Exception as err:
                error(err)
        
        task_n = tkinter.StringVar()
        task_n.set('1')
        show_one_task()
        task_choice = tkinter.Spinbox(delete_window,
                                      from_=1,
                                      to=len(todoList),
                                      textvariable=task_n,
                                      command=show_one_task)
        task_choice.grid(row=1, column=0)
        
        def delete():
            """
            Удаление задания
            """
            try:
                todoList.remove(todoList[int(task_n.get())-1])
                writer('tasks.json', todoList)
                delete_window.destroy()
                show_task()
            except Exception as err:
                error(err)
            
        to_delete = tkinter.Button(delete_window, text='Удалить', command=delete)
        to_delete.grid(row=2, column=0)
        
        delete_window.mainloop()
    except Exception as err:
        error(err)

def show_task():
    """
    Вывод заданий на экран (можно легко переделать под показ при нажатии,
    но я решила сделать автообновление при добавлении и удалении задачи)
    """
    try:
        count = 0
        temp_task = ''
        filter_string = filter_text.get()
        for task in todoList:
            count += 1
            if True in list(map(lambda x: filter_string in x, list(task.values()))):
                temp_task = temp_task + str(count) + " задача\n"
                for name in task:
                    temp_task = temp_task + '\t' + name + ': ' + task[name] + '\n'
        list_task.set(temp_task)
    except Exception as err:
        error(err)

def clear_filter():
    try:
        filter_text.set('')
        show_task()
    except Exception as err:
        error(err)

try:
    window = tkinter.Tk()
    window.geometry('+300+200')
    window.title("Менеджер задач")
    #window.lift()
    #window.minsize(600, 200)
    
    todoList = list(reader('tasks.json'))
    #вся левая часть
    frame_left = tkinter.Frame(window)
    frame_left.grid(row=0, column=0, sticky=tkinter.N)
    #верх левой
    frame_left_top = tkinter.Frame(frame_left)
    frame_left_top.pack(side='top')
    """
    Названия полей ввода
    """
    label_name = tkinter.Label(frame_left_top, text='Задача')
    label_name.grid(row=0, column=0, sticky=tkinter.E)
    
    label_cat = tkinter.Label(frame_left_top, text='Категория')
    label_cat.grid(row=1, column=0, sticky=tkinter.E)
    
    label_time = tkinter.Label(frame_left_top, text='Время')
    label_time.grid(row=2, column=0, sticky=tkinter.E)
    """
    Поля ввода
    """
    task = tkinter.StringVar()
    entry_task = tkinter.Entry(frame_left_top, textvariable=task)
    entry_task.grid(row=0, column=1)
    
    cat = tkinter.StringVar()
    entry_cat = tkinter.Entry(frame_left_top, textvariable=cat)
    entry_cat.grid(row=1, column=1)
    
    time = tkinter.StringVar()
    entry_time = tkinter.Entry(frame_left_top, textvariable=time)
    entry_time.grid(row=2, column=1)
    #низ левой
    frame_left_bottom = tkinter.Frame(frame_left, borderwidth=4)
    frame_left_bottom.pack(side='bottom')
    """
    Уведомление о добавлении задачи
    """
    info = tkinter.StringVar()
    announcer = tkinter.Label(frame_left_bottom, textvariable=info)
    announcer.grid(row=0, column=0)
    """
    Кнопки
    """
    button_add = tkinter.Button(frame_left_bottom,
                                text='Добавить задачу',
                                command=add_task)
    button_add.grid(row=1, column=0)
    
    button_delete = tkinter.Button(frame_left_bottom,
                                   text='Удалить задачу',
                                   command=delete_task)
    button_delete.grid(row=2, column=0)
    '''
    button_show = tkinter.Button(frame_left_bottom,
                                 text='Вывести задачи',
                                 command=show_task)
    button_show.grid(row=3, column=0)
    '''
    button_exit = tkinter.Button(frame_left_bottom,
                                 text='Выход',
                                 command=window.destroy)
    button_exit.grid(row=4, column=0)
    #правая часть
    """
    Вывод задач
    """
    frame_right = tkinter.Frame(window, borderwidth=10)
    frame_right.grid(row=0, column=1, sticky=tkinter.N)

    frame_filter = tkinter.Frame(frame_right)
    frame_filter.grid(row=0, column=0)

    button_filter = tkinter.Button(frame_filter,
                                   text='Фильтр',
                                   command=show_task)
    button_filter.grid(row=0, column=0, sticky=tkinter.W, ipadx=20)

    button_notfilter = tkinter.Button(frame_filter,
                                   text='Убрать фильтр',
                                   command=clear_filter)
    button_notfilter.grid(row=2, column=0, sticky=tkinter.W, ipadx=20)

    filter_text = tkinter.StringVar()
    filter_text.set('')
    entry_filter = tkinter.Entry(frame_filter,
                                 textvariable=filter_text)
    entry_filter.grid(row=0, column=1)
    
    list_task = tkinter.StringVar()
    printed_task = tkinter.Label(frame_right, textvariable=list_task, justify=tkinter.LEFT)
    printed_task.grid(row=1, column=0)
    show_task()
    window.mainloop()
except Exception as err:
    error(err)
