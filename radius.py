import tkinter
from math import pi

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

def volume():
    """
    Функция для подсчета объема
    """
    try:
        result.set(round(4/3*pi*(radius.get()**3), 3))
        unconnected_radius.set(radius.get()) #данная переменная защищает от случайного сохранения радиуса, который был введен, но не посчитан
    except Exception as err:
        error(err)

def reader_txt():
    pass

def writer_txt():
    """
    Запись в txt файл
    """
    try:
        with open('volume_data.txt', 'a', encoding='utf-8') as file:
            text_to_add = 'Радиус: '+str(unconnected_radius.get())+' Объем: '+str(result.get())+'\n'
            file.write(text_to_add)
    except Exception as err:
        error(err)

def reader_html():
    """
    Чтение из html-файла
    """
    with open('volume_data.html', 'r', encoding='utf-8') as file:
            lines = file.readlines()
    return lines       

def writer_html():
    """
    Добавление результата в html файл, при этом считываются 
    все уже существующие строки без последних трех, чтобы 
    можно было добавить удобно новый результат
    """
    try:
        text_to_add = ''.join(reader_html()[:-3])
        with open('volume_data.html', 'w', encoding='utf-8') as file:
            text_to_add += '        Радиус: '+str(unconnected_radius.get())+' Объем: '+str(result.get())+'<br>\n'
            text_to_add += '        </p>\n    </body>\n</html>'
            file.write(text_to_add)
    except Exception as err:
        error(err)

def writer():
    """
    Функция для определения того, в какой файл записывать результат
    """
    try:
        if where.get()!='HTML':
            writer_txt()
        else:
            writer_html()
        info.set('Сохранено')
        announcer.after(2000, lambda: info.set(''))
    except Exception as err:
        error(err)

try:
    window = tkinter.Tk()
    window.title('Программа для вычисления объема сферы')

    left_frame = tkinter.Frame(window)
    left_frame.grid(row=0, column=0)
    
    data = tkinter.Frame(left_frame)
    data.grid(row=0, column=0)

    data_name = tkinter.Label(data, text='Введите радиус:')
    data_name.grid(row=0, column=0, sticky=tkinter.W)

    radius = tkinter.DoubleVar()
    unconnected_radius = tkinter.DoubleVar()
    data_entry = tkinter.Entry(data, textvariable=radius)
    data_entry.grid(row=0, column=1)

    result_name = tkinter.Label(data, text='Результат\nвычислений:')
    result_name.grid(row=1, column=0, sticky=tkinter.W)

    result = tkinter.DoubleVar()
    result_number = tkinter.Label(data, textvariable=result)
    result_number.grid(row=1, column=1)

    button_frame = tkinter.Frame(left_frame)
    button_frame.grid(row=1, column=0)

    button_find = tkinter.Button(button_frame,
                                 text='Вычислить',
                                 command=volume)
    button_find.grid(row=0, column=0)

    save_frame = tkinter.Frame(left_frame)
    save_frame.grid(row=2, column=0)

    button_save = tkinter.Button(save_frame,
                                 text='Сохранить',
                                 command=writer)
    button_save.grid(row=0, column=0)

    where = tkinter.StringVar()
    where.set('Teкст')
    save_option = tkinter.OptionMenu(save_frame, where, 'Текст', 'HTML')
    save_option.grid(row=0, column=1)

    info = tkinter.StringVar()
    announcer = tkinter.Label(save_frame, textvariable=info)
    announcer.grid(row=1, column=0)
    
    window.mainloop()
except Exception as err:
    error(err)
