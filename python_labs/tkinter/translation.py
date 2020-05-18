import tkinter

class translateGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.translation = tkinter.StringVar()
        self.translation.set('')
        self.translation_label = tkinter.Label(self.top_frame,
                   textvariable=self.translation)
        self.translation_label.pack()

        self.sinister_button = tkinter.Button(self.bottom_frame,
                                          text='sinister',
                                          command=self.sinister)
        self.dexter_button = tkinter.Button(self.bottom_frame,
                                          text='dexter',
                                   command=self.dexter)
        self.medium_button = tkinter.Button(self.bottom_frame,
                                          text='medium',
                                   command=self.medium)

        self.sinister_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.medium_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def sinister(self):
        self.translation.set('зловещий')
    def dexter(self):
        self.translation.set('правый')
    def medium(self):
        self.translation.set('средний')

translate = translateGUI()
