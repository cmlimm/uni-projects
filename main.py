from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import time

class ClocksGUI:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("640x480")
        self.main_window.title("Clock")

        self.chosen_alarm_label = Label(self.main_window, \
        text="Будильник не установлен", font=("Times", 20))
        self.chosen_alarm_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.label = Label(self.main_window, text="", font=("Times", 50))
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.dec_hours_button = Button(self.main_window, text="-H", \
        command=self.dec_hour, height=2, width=3)
        self.dec_hours_button.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.dec_minutes_button = Button(self.main_window, text="-M", \
        command=self.dec_minute, height=2, width=3)
        self.dec_minutes_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.inc_hours_button = Button(self.main_window, text="+H", \
        command=self.inc_hour, height=2, width=3)
        self.inc_hours_button.place(relx=0.4, rely=0.7, anchor=CENTER)
        self.inc_minutes_button = Button(self.main_window, text="+M", \
        command=self.inc_minute, height=2, width=3)
        self.inc_minutes_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.alarm_button = Button(self.main_window, text="A", \
        command=self.alarm_gui, height=2, width=3)
        self.alarm_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.hour_counter = 0
        self.minute_counter = 0
        self.click_counter = 0
        self.alarm_hour = 0
        self.alarm_minute = 0
        self.chosen_alarm_hour = 0
        self.chosen_alarm_minute = 0

        self.tick()
        self.main_window.mainloop()


    def tick(self):
        self.current_hour = (int(time.strftime("%I")) + 12 + \
        self.hour_counter)%24
        self.current_minute = (int(time.strftime("%M")) + \
        self.minute_counter)%60
        self.current_second = int(time.strftime("%S"))

        if self.current_hour == self.chosen_alarm_hour and \
        self.current_minute == self.chosen_alarm_minute and \
        self.current_second == 0:
            messagebox.showinfo("Внимание", "Будильник!")

        self.current_time = time.strftime("%I:%M:%S")

        self.label.config(text=str(self.current_hour).zfill(2) + ":" + \
        str(self.current_minute).zfill(2) + ":" + \
        str(self.current_second).zfill(2))
        self.label.after(200, self.tick)

    def inc_hour(self):
        self.hour_counter += 1
        self.tick()

    def inc_minute(self):
        self.minute_counter += 1
        self.tick()

    def dec_hour(self):
        self.hour_counter -= 1
        self.tick()

    def dec_minute(self):
        self.minute_counter -= 1
        self.tick()

    def alarm_gui(self):
        self.alarm_window = Tk()
        self.alarm_window.geometry("320x240")
        self.alarm_window.title("Alarm")

        self.alarm_label = Label(self.alarm_window, \
        text="00:00", font=("Times", 50))
        self.alarm_label.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.alarm_dec_hours_button = Button(self.alarm_window, text="-H", \
        command=self.dec_alarm_hour, height=2, width=3)
        self.alarm_dec_hours_button.place(relx=0.4, rely=0.6, anchor=CENTER)
        self.alarm_dec_minutes_button = Button(self.alarm_window, text="-M", \
        command=self.dec_alarm_minute, height=2, width=3)
        self.alarm_dec_minutes_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.alarm_inc_hours_button = Button(self.alarm_window, text="+H", \
        command=self.inc_alarm_hour, height=2, width=3)
        self.alarm_inc_hours_button.place(relx=0.4, rely=0.8, anchor=CENTER)
        self.alarm_inc_minutes_button = Button(self.alarm_window, text="+M", \
        command=self.inc_alarm_minute, height=2, width=3)
        self.alarm_inc_minutes_button.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.set_alarm_button = Button(self.alarm_window, text="S", \
        command=self.set_alarm, height=2, width=3)
        self.set_alarm_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.alarm_window.mainloop()

    def inc_alarm_hour(self):
        self.alarm_hour = (self.alarm_hour + 1)%24
        self.alarm_label.config(text=str(self.alarm_hour).zfill(2) + ":" + \
        str(self.alarm_minute).zfill(2))

    def inc_alarm_minute(self):
        self.alarm_minute = (self.alarm_minute + 1)%60
        self.alarm_label.config(text=str(self.alarm_hour).zfill(2) + ":" + \
        str(self.alarm_minute).zfill(2))

    def dec_alarm_hour(self):
        self.alarm_hour = (self.alarm_hour - 1)%24
        self.alarm_label.config(text=str(self.alarm_hour).zfill(2) + ":" + \
        str(self.alarm_minute).zfill(2))

    def dec_alarm_minute(self):
        self.alarm_minute = (self.alarm_minute - 1)%60
        self.alarm_label.config(text=str(self.alarm_hour).zfill(2) + ":" + \
        str(self.alarm_minute).zfill(2))

    def set_alarm(self):
        self.chosen_alarm_hour = self.alarm_hour
        self.chosen_alarm_minute = self.alarm_minute
        self.alarm_hour = 0
        self.alarm_minute = 0

        self.chosen_alarm_label.config(text="Будильник установлен на " + \
        str(self.chosen_alarm_hour).zfill(2) + ":" + \
        str(self.chosen_alarm_minute).zfill(2))
        self.alarm_window.destroy()


clocks = ClocksGUI()
