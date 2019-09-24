from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import time
import pygame

class ClocksGUI:
    # основное окно
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("640x480")
        self.main_window.title("Clock")

        self.chosen_alarm_label = Label(self.main_window, \
        text="Будильник не установлен", font=("Times", 20))
        self.chosen_alarm_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.label = Label(self.main_window, text="", font=("Times", 50))
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # кнопки уменьшения часов/минут
        self.dec_hours_button = Button(self.main_window, text="-H", \
        command=self.dec_hour, height=2, width=3)
        self.dec_hours_button.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.dec_minutes_button = Button(self.main_window, text="-M", \
        command=self.dec_minute, height=2, width=3)
        self.dec_minutes_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        # кнопки увеличения часов/минут
        self.inc_hours_button = Button(self.main_window, text="+H", \
        command=self.inc_hour, height=2, width=3)
        self.inc_hours_button.place(relx=0.4, rely=0.7, anchor=CENTER)
        self.inc_minutes_button = Button(self.main_window, text="+M", \
        command=self.inc_minute, height=2, width=3)
        self.inc_minutes_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        # кнопка настройки будильника
        self.alarm_button = Button(self.main_window, text="A", \
        command=self.alarm_gui, height=2, width=3)
        self.alarm_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.is_alarm_set = False
        self.chosen_alarm_hour = 0
        self.chosen_alarm_minute = 0

        self.current_hour = int(time.strftime("%H"))
        self.current_minute = int(time.strftime("%M"))
        self.current_second = int(time.strftime("%S"))
        self.current_time = time.strftime("%H:%M:%S")

        pygame.init()
        self.alarm_sound = pygame.mixer.Sound('alarm.ogg')

        self.tick()
        self.main_window.mainloop()


    # функции для изменения отображения времени часов
    def change_clock_label(self):
        self.label.config(text=str(self.current_hour).zfill(2) + ":" + \
        str(self.current_minute).zfill(2) + ":" + \
        str(self.current_second).zfill(2))

    # функции для изменения часов/минут, tick чтобы не было задержки при изменении
    def inc_hour(self):
        self.current_hour = (self.current_hour + 1)%24
        self.change_clock_label()
        self.tick()

    def inc_minute(self):
        self.current_minute = (self.current_minute + 1)%60
        self.change_clock_label()
        self.tick()

    def dec_hour(self):
        self.current_hour = (self.current_hour - 1)%24
        self.change_clock_label()
        self.tick()

    def dec_minute(self):
        self.current_minute = (self.current_minute - 1)%60
        self.change_clock_label()
        self.tick()

    # Метод обновления времени
    #
    # Сразу после запуска приложения время такое же, как на компьютере
    # пользователя
    #
    # Каждые 200 миллисекунд время пытается обновиться
    def tick(self):
        if self.current_time != time.strftime("%H:%M:%S"):
            self.current_time = time.strftime("%H:%M:%S")
            self.current_second = (self.current_second + 1)%60
            if self.current_second == 0:
                self.current_minute = (self.current_minute + 1)%60
                if self.current_minute == 0:
                    self.current_hour = (self.current_hour + 1)%24

            # проверка на совпадение с временем будильника
            if self.current_hour == self.chosen_alarm_hour and \
            self.current_minute == self.chosen_alarm_minute \
            and self.current_second == 0 and self.is_alarm_set:
                self.alarm()

            self.change_clock_label()

        self.label.after(200, self.tick)

    # функция для окна сработавшего будильника
    def alarm(self):
        self.alarm_sound.play()
        answer = messagebox.askyesno("Будильник", "Перенести на 10 минут?")
        if answer == True:
            if self.chosen_alarm_minute + 10 >= 60:
                self.chosen_alarm_hour = (self.chosen_alarm_hour + 1)%24
            self.chosen_alarm_minute = (self.chosen_alarm_minute + 10)%60
            self.change_chosen_alarm_label()
        else:
            self.chosen_alarm_hour = 0
            self.chosen_alarm_minute = 0
            self.is_alarm_set = False
            self.chosen_alarm_label.config(text='Будильник не установлен')
        self.alarm_sound.stop()

    # Окно настройки будильника
    def alarm_gui(self):
        # чтобы нельзя было создать несколько окон настройки будильника
        # временно отключается функция кнопки настройки будильника
        self.alarm_button = Button(self.main_window, text="A", height=2, width=3)
        self.alarm_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.alarm_window = Tk()
        self.alarm_window.geometry("320x240")
        self.alarm_window.title("Alarm")

        self.alarm_hour = 0
        self.alarm_minute = 0

        self.alarm_label = Label(self.alarm_window, \
        text="00:00", font=("Times", 50))
        self.alarm_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        # кнопки уменьшение часов/минут будильника
        self.alarm_dec_hours_button = Button(self.alarm_window, text="-H", \
        command=self.dec_alarm_hour, height=2, width=3)
        self.alarm_dec_hours_button.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.alarm_dec_minutes_button = Button(self.alarm_window, text="-M", \
        command=self.dec_alarm_minute, height=2, width=3)
        self.alarm_dec_minutes_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        # кнопки увеличение часов/минут будильника
        self.alarm_inc_hours_button = Button(self.alarm_window, text="+H", \
        command=self.inc_alarm_hour, height=2, width=3)
        self.alarm_inc_hours_button.place(relx=0.4, rely=0.8, anchor=CENTER)
        self.alarm_inc_minutes_button = Button(self.alarm_window, text="+M", \
        command=self.inc_alarm_minute, height=2, width=3)
        self.alarm_inc_minutes_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        # кнопка установки будильника
        self.set_alarm_button = Button(self.alarm_window, text="S", \
        command=self.set_alarm, height=2, width=3)
        self.set_alarm_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.alarm_window.mainloop()

    # функции для изменения отображения времени будильника в окне будильника
    def change_alarm_label(self):
        self.alarm_label.config(text=str(self.alarm_hour).zfill(2) + ":" + \
        str(self.alarm_minute).zfill(2))

    # функции для изменения часов/минут будильника
    def inc_alarm_hour(self):
        self.alarm_hour = (self.alarm_hour + 1)%24
        self.change_alarm_label()

    def inc_alarm_minute(self):
        self.alarm_minute = (self.alarm_minute + 1)%60
        self.change_alarm_label()

    def dec_alarm_hour(self):
        self.alarm_hour = (self.alarm_hour - 1)%24
        self.change_alarm_label()

    def dec_alarm_minute(self):
        self.alarm_minute = (self.alarm_minute - 1)%60
        self.change_alarm_label()

    # функция для изменения отображения времени будильника в окне часов
    def change_chosen_alarm_label(self):
        self.chosen_alarm_label.config(text="Будильник установлен на " + \
        str(self.chosen_alarm_hour).zfill(2) + ":" + \
        str(self.chosen_alarm_minute).zfill(2))

    # функция установки будильника и выхода из окна будильника
    def set_alarm(self):
        self.chosen_alarm_hour = self.alarm_hour
        self.chosen_alarm_minute = self.alarm_minute
        self.is_alarm_set = True
        self.change_chosen_alarm_label()

        # восстановление функции создания окна настройки будильника
        self.alarm_button = Button(self.main_window, text="A", \
        command=self.alarm_gui, height=2, width=3)
        self.alarm_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.alarm_window.destroy()

clocks = ClocksGUI()
