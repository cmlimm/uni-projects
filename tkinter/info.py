# Эта программа показывает два элемента Label с текстом.

import tkinter

class MyGUI:
    def __init__(self):
        # Создать элемент интерфейса главного окна.
        self.main_window = tkinter.Tk()

        self.first_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.first_lane = tkinter.StringVar()
        self.first_lane.set('')
        # Создать два элемента интерфейса Label.
        self.label1 = tkinter.Label(self.first_frame,
                                    textvariable=self.first_lane,
                                    justify=tkinter.LEFT)

        # Вызвать метод pack обоих элементов интерфейса Label.
        self.label1.pack()

        # Создать кнопку 'OK' и кнопку 'Выйти'.
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='Показать текст',
                                        command=self.show_text)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Выйти',
                                 command=self.main_window.destroy)

        # Упаковать элементы Button.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.first_frame.pack()
        self.bottom_frame.pack()

        # Войти в главный цикл tkinter.
        tkinter.mainloop()

    def show_text(self):
        self.first_lane.set('Стивен Маркус\n274 Бейли\nУэйнзвилль, Северная Каролина 27999')

# Создать экземпляр класса MyGUI.
my_gui = MyGUI()
