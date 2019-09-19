from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import time
import datetime

class ClocksGUI:
    def __init__(self):

        self.main_window = Tk()
        self.main_window.geometry("640x480")
        self.main_window.title("Clock")

        self.temp_hour_counter = IntVar()
        self.temp_minute_counter = IntVar()

        self.temp_hour_counter.set(0)
        self.temp_minute_counter.set(0)

        self.label_alarm = Label(self.main_window,
                                 text="Будильник установлен на ", font=("Times", 20))
        self.label_alarm.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.label = Label(self.main_window, text="", font=("Times", 50))
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)
        #self.main_window.title_font = tkfont.Font(family = "Times", size = 100, weight = "bold", slant = "italic")

        self.hours_button = Button(self.main_window, text="H", command=self.add_hour, height=2, width=3)
        self.hours_button.place(relx=0.4, rely=0.6, anchor=CENTER)

        self.minutes_button = Button(self.main_window, text="M", command=self.add_minute, height=2, width=3)
        self.minutes_button.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.alarm_button = Button(self.main_window, text="A", command=self.alarm, height=2, width=3)
        self.alarm_button.place(relx=0.6, rely=0.6, anchor=CENTER)

        self.hour_counter = 0
        self.minute_counter = 0
        self.click_counter = 0

        self.tick()

        self.main_window.mainloop()

    def tick(self):
        self.current_hour = (int(time.strftime("%I"))+ 12 + self.hour_counter)%24
        self.current_minute = (int(time.strftime("%M")) + self.minute_counter)%60
        self.current_second = int(time.strftime("%S"))
        self.current_time = time.strftime("%I:%M:%S")
        self.label.config(text=str(self.current_hour)+":"+str(self.current_minute)+":"+str(self.current_second))
        self.label.after(200, self.tick)

    def add_hour(self):
        self.hour_counter +=1
        self.tick()

    def add_minute(self):
        self.minute_counter +=1
        self.tick()

    def alarm(self):
        self.click_counter = (self.click_counter + 1)%3


clocks = ClocksGUI()
