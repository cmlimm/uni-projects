# Эта программа демонстрирует группу элементов Radiobutton.
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Создать главное окно.
        self.main_window = tkinter.Tk()

        # Создать две рамки. Одну для элементов Radiobutton
        # и еще одну для обычных элементов Button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Создать объект IntVar для использования с
        # элементами Radiobutton.
        self.radio_var = tkinter.IntVar()

        # Назначить объекту IntVar значение 1.
        self.radio_var.set(1)

        # Создать элементы Radiobutton в рамке top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Дневное время (6:00-17:59)',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Вечернее время (18:00-23:59)',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Непиковый период (0:00-5:59)',
                                       variable=self.radio_var,
                                       value=3)

        self.prompt_label = tkinter.Label(self.top_frame,
                             text='Введите количество минут:')
        self.time_entry = tkinter.Entry(self.top_frame,
                                        width=10)

        # Упаковать элементы Radiobutton.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Упаковать элементы ввода минут.
        self.prompt_label.pack(side='left')
        self.time_entry.pack(side='left')

        # Создать кнопку 'OK' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='OK',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                command=self.main_window.destroy)

        # Упаковать элементы Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Упаковать рамки.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Запустить главный цикл.
        tkinter.mainloop()

    # Метод show_choice является функцией обратного вызова
    # для кнопки OK.
    def show_choice(self):
        choice = str(self.radio_var.get())
        time = int(self.time_entry.get())
        if choice == '1':
            self.payment = round(time*10/100, 2)
        elif choice == '2':
            self.payment = round(time*12/100, 2)
        elif choice == '3':
            self.payment = round(time*5/100, 2)
        tkinter.messagebox.showinfo('Выбор', 'Ваши затраты: $' +
                                    str(self.payment))

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
