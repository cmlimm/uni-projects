from tkinter import font as tkfont
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from utils import *
import os

class App:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("1280x640")
        self.main_window.title("Notes")

        self.main_frame = Frame(self.main_window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.folder = 'notes'
        self.get_notes()
        self.note_font = tkfont.Font(family="Arial", size=20)

        self.delete_button = Button(self.main_frame, text='Удалить', command=self.delete_note)
        self.delete_button.grid(row=0, column=0)

        self.add_button = Button(self.main_frame, text='Добавить', command=self.add_note)
        self.add_button.grid(row=0, column=1)

        # список заметок
        self.note_listbox = Listbox(self.main_frame, borderwidth=1, width=25, height=24,
                                    font=self.note_font)
        self.note_listbox.grid(row=1, column=0, columnspan=2)

        # возможность скроллить список заметок
        self.note_listbox_scroll = Scrollbar(self.main_frame, orient=VERTICAL,
                                      command=self.note_listbox.yview)
        self.note_listbox.configure(yscrollcommand=self.note_listbox_scroll.set)
        self.note_listbox_scroll.grid(row=1, column=3)

        # добавление списка заметок в Listbox
        self.set_note_listbox()

        # связка выбор заметки -- отображение заметки
        self.note_listbox.bind('<<ListboxSelect>>', self.select_note)

        # поле заметок
        self.note_text = Text(self.main_frame, width=70, height=26,
                                    wrap=WORD, font=self.note_font,
                                    highlightbackground='black',
                                    highlightthickness=0.5)
        self.note_text.grid(row=0, column=4, rowspan=2)

        self.note_text.bind('<KeyRelease>', self.onModification)
        self.note_text.bind('<Button-2>', self.popup)

        self.predictions = Menu(self.main_frame)

        # возможность скроллить заметку
        self.note_scrollbar = Scrollbar(self.main_frame, orient=VERTICAL,
                                        command=self.note_text.yview)
        self.note_scrollbar.grid(row=0, column=5, sticky=N+S+E+W)
        self.note_text["yscrollcommand"]=self.note_scrollbar.set

        self.main_window.mainloop()

    def predict_words(self, text):
        pred = top_n(text, 3, all_words_norep, next_words, words_prob)
        return pred

    def correct_word(self, text, word):
        pred = top_n(text, 1, all_words_norep, next_words, words_prob, word)
        n_mist = 1
        if pred == 0:
            n_mist = 2
        mist = top_n_mistakes(text, n_mist, word, all_words_norep, next_words, words_prob)
        spl = ' '.join(split_sent(word, words_prob))
        return pred + mist + [spl]

    def add_word(self, word):
        self.note_text.delete("1.0", "end")
        if self.state == 'correction':
            self.note_text.insert(1.0, self.text[:-len(self.old)-1] + word)
        if self.state == 'prediction':
            self.note_text.insert(1.0, self.text.strip() + ' ' + word)

    def clean_text(self, text):
        marks = re.compile(r'\.|\:|;|\?|!|--|"|,|–|»|«')
        text = re.sub(marks, '', text).lower()
        return text.split()

    def first(self):
        self.add_word(self.suggestions[0])

    def second(self):
        self.add_word(self.suggestions[1])

    def third(self):
        self.add_word(self.suggestions[2])

    def fourth(self):
        self.add_word(self.suggestions[4])

    def popup(self, event):
        self.text = self.note_text.get(1.0, END)
        if self.text[-2] == ' ' or self.text[-2] == '\n' or self.text[-2] == '\t':
            self.state = 'prediction'
            self.suggestions = self.predict_words(self.clean_text(self.text)[-5:])
        else:
            self.state = 'correction'
            cleaned = self.clean_text(self.text)
            self.old = cleaned[-1]
            self.suggestions = self.correct_word(cleaned[-5:-1], self.old)

        funcs = [self.first, self.second, self.third, self.fourth]
        self.predictions.delete(0, END)
        for i in range(len(self.suggestions)):
            self.predictions.add_command(label=self.suggestions[i],
                                         command=funcs[i])


        self.predictions.post(event.x_root, event.y_root)

    def onModification(self, event=None):
        text = self.note_text.get(1.0, END)
        write_file(self.files[self.index], text)
        self.get_notes()
        self.note_listbox.delete(self.index)
        self.note_listbox.insert(self.index, text[:30])


    def delete_note(self, event=None):
        try:
            os.remove(self.files[self.index])
            self.get_notes()
            self.note_listbox.delete(self.index)
        except:
            pass

    def add_note(self, event=None):
        note_number = int(self.files[-1][len(self.folder)+5:-4]) + 1
        note_name = self.folder + '/note' + str(note_number) + '.txt'
        write_file(note_name, '')
        self.get_notes()
        self.note_listbox.insert(END, '')

    def select_note(self, event=None):
        self.index = self.note_listbox.curselection()[0]
        self.note_text.delete("1.0", "end")
        self.note_text.insert(1.0, self.notes[self.index])

    def get_notes(self):
        self.notes = []
        self.files = []
        for root, dirs, files in os.walk(self.folder):
            for file in files:
                self.files.append(self.folder + '/' + file)
        self.files = sorted(self.files)

        for file in self.files:
            self.notes.append(read_file(file))

    def set_note_listbox(self):
        for note in self.notes:
            self.note_listbox.insert(END, note[:30])

app = App()
