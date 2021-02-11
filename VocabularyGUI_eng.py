from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import random

window = Tk()

window.title("Vocabulary Trainer")
window.geometry('1100x700')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control, style='new.TFrame')
tab2 = ttk.Frame(tab_control, style='new.TFrame')
tab3 = ttk.Frame(tab_control, style='new.TFrame')

s = ttk.Style()
s.configure('new.TFrame', background='navajowhite')

tab_control.add(tab1, text='Home')
tab_control.add(tab2, text='Vocabulary')
tab_control.add(tab3, text='Exam')


# Tab 1 : first Window
'''First Window'''


def Welcome():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if (x2 < 0 or y1 < 0):
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height() // 2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000 // fps, Welcome)


canvas = Canvas(tab1, bg='bisque')
canvas.pack(anchor=N, expand=1, pady=40)
text_var = "WELCOME TO THE VOCABULARY TRAINER"
text = canvas.create_text(0, -2000, text=text_var, font=('comic sans ms', 26, 'bold'), fill='dark olive green',tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
canvas['width'] = 550
canvas['height'] = 64
fps = 80  # Schnelligkeit der Animation einstellen
Welcome()


description = Label(tab1, text="""Description:\n
This is a vocabulary trainer containing a small standard vocabulary list.\nHere you can find foreign words and their meanings, backed up with an example."\n
Tab "Vocabulary": - study all the vocabulary and add new ones!\nTab "Exam": - take the vocabulary exam and put your language skills to the test""",
             bg="bisque", padx=20, pady=20, font=("comic sans ms", 13, ""))
description.place(relx=0.5, rely=0.25, anchor="n")

glhf = Label(tab1, text="Good Luck Have Fun!", bg="navajowhite", font=("comic sans ms", 22, "bold"), fg="dark olive green")
glhf.place(relx=0.5, rely=0.63, anchor="n")

rules = Label(tab1, text="""rules:\n
"ü" = "ue"\n"ä" = "ae"\n"ö" = "oe"\n"ß" = "ss" """,bg="navajowhite",
             font=("corbel", 13, "bold"))
rules.place(relx=0.5, rely=0.72, anchor="n")

made_by = Label(tab1, text="@Developed by Angel Mechkarov", bg="navajowhite", font=("Miriam Mono CLM", 11, ""),
             fg="gray30")
made_by.place(relx=0.5, rely=0.94, anchor="n")


class Vocabulary:
    def __init__(self, english, german, example):
        self.english = english
        self.german = german
        self.example = example

    def row(self):
        tree_view.insert("", "end", text="L1",
                     values=(self.english, self.german, self.example))


vocabulary_entry_list = []

file_name = "./vocabulary.txt"
if os.path.isfile(file_name):
    vocabulary_words = open(file_name)

    for line in vocabulary_words:
        vocabulary_words = line.split(",")
        vocabulary_entry_list.append(Vocabulary(vocabulary_words[0].strip(), vocabulary_words[1].strip(),vocabulary_words[2].strip()))


#Tab 2 / second Window
'''Second Window'''

tree_view = ttk.Treeview(tab2, selectmode='browse')
tree_view.pack(side='top', ipady="80")

scrollbar = ttk.Scrollbar(tab2, orient="vertical", command=tree_view.yview)

scrollbar.place(relx=0.10, rely=0.01, anchor="n", height=370)

tree_view.configure(xscrollcommand=scrollbar.set)

tree_view["columns"] = ("1", "2", "3")
tree_view['show'] = 'headings'

tree_view.column("1", width=170, anchor='center')
tree_view.column("2", width=170, anchor='center')
tree_view.column("3", width=120, anchor='center')

tree_view.heading("1", text="Englisch")
tree_view.heading("2", text="Deutsch")
tree_view.heading("3", text="Beispiel")

tree_view.column('1', stretch=tk.YES)
tree_view.column('2', stretch=tk.YES)
tree_view.column('3', width="500")


for vocabulary_entry in vocabulary_entry_list:
    print(vocabulary_entry.row())


entry_english = Entry(tab2, font=12, width=25)
entry_english.place(relx=0.43, rely=0.71, anchor="n")

entry_german = Entry(tab2, font=12, width=25)
entry_german.place(relx=0.43, rely=0.81, anchor="n")

entry_example = Entry(tab2, font=12, width=40)
entry_example.place(relx=0.49, rely=0.91, anchor="n")


label_english = Label(tab2, text="english word:", bg="navajowhite", font=("corbel", 13, "bold"))
label_english.place(relx=0.23, rely=0.71, anchor="n")

label_german = Label(tab2, text="german word:", bg="navajowhite", font=("corbel", 13, "bold"))
label_german.place(relx=0.23, rely=0.81, anchor="n")

label_example = Label(tab2, text="example:", bg="navajowhite", font=("corbel", 13, "bold"))
label_example.place(relx=0.23, rely=0.91, anchor="n")


with open(file_name,"r") as f:
    first_words = [line.split(",",maxsplit=1)[0] for line in f if line.strip()]
#print(first_words)

with open(file_name,"r") as f:
    second_words = [line.split(",",maxsplit=2)[1] for line in f if line.strip()]
#print(second_words)


#Filter
'''_Entry Word Filter_ => to stop repeating same words in dictionary'''

existing_word = Label(tab2)


def save():
    global existing_word

    existing_word.destroy()

    if entry_english.get() in first_words:
        existing_word = Label(tab2,text="ERROR: given word already exists",font=("corbel",14,"bold"),bg="navajowhite",fg="red")
        existing_word.place(relx=0.8,rely=0.9,anchor="n")
    else:
        tree_view.insert("", "end", text="L1",
                         values=(entry_english.get(), entry_german.get(), entry_example.get()))

        with open(file_name, "a+") as save_words:
            save_words.write(f"\n{entry_english.get()},{entry_german.get()},{entry_example.get()}")

        entry_english.delete(0, END)
        entry_german.delete(0, END)
        entry_example.delete(0, END)


def delete():
    x = tree_view.selection()[0]
    tree_view.delete(x)


save_button = Button(tab2, text="SAVE", bg="dark olive green", fg="yellow", font=("rubik", 13, "bold"),
                     activebackground="dark green", activeforeground="orange", height=1, width=10, cursor="plus",
                     relief="raised", command=save)
save_button.place(relx=0.65, rely=0.71, anchor="n")

delete_button = Button(tab2, text="DELETE", bg="dark olive green", fg="yellow", font=("rubik", 10, "bold"),
                       activebackground="dark green", activeforeground="orange", height=1, width=10, cursor="plus",
                       relief="raised", command=delete)
delete_button.place(relx=0.65, rely=0.81, anchor="n")


info_save = Label(tab2,text='*How to use:*\n Click on "SAVE"(button) to \nadd the GER/ENG-inputs to the vocabulary list',
                  bg="navajowhite", font=("corbel", 8, ""))
info_save.place(relx=0.84, rely=0.69, anchor="n")

info_delete = Label(tab2,text='*How to use:*\n Click on "DELETE"(button) to \ndelete a word from the vocabulary list',
                    bg="navajowhite", font=("corbel", 8, ""))
info_delete.place(relx=0.84, rely=0.79, anchor="n")

search_open_text = Label(tab2, text='Search for a word in the list:', bg="navajowhite", font=("corbel", 13, "italic"))
search_open_text.place(relx=0.3, rely=0.6, anchor="n")


def openNewWindow():
    newWindow = Toplevel(tab2,bg="cornsilk2")
    newWindow.title("VSE - Vocabulary Search Engine")
    newWindow.geometry("400x400")

    search_text = Label(newWindow, text="Search for a word",bg="cornsilk2",fg="dark green",font=("", 16, "bold"))
    search_text.place(relx=0.5, rely=0.03, anchor="n")

    description_search = Label(newWindow, text="Enter a word\n to receive the translation", bg="cornsilk2",fg="black", font=("", 12, "italic"))
    description_search.place(relx=0.5, rely=0.18, anchor="n")

    give_word_text = Label(newWindow, text="word:", bg="cornsilk2",fg="black", font=("", 12, "bold"))
    give_word_text.place(relx=0.5, rely=0.37, anchor="n")

    search_word = Entry(newWindow,font=12, width=22)
    search_word.place(relx=0.5, rely=0.47, anchor="n")

    global english_word_search
    global german_word_search
    global error_search

    english_word_search = Label(newWindow)
    german_word_search = Label(newWindow)
    error_search = Label(newWindow)

    def sucher():
        global english_word_search
        global german_word_search
        global error_search

        english_word_search.destroy()
        german_word_search.destroy()
        error_search.destroy()

        if search_word.get() in first_words:
            word_index = first_words.index(search_word.get())
            english_word_search = Label(newWindow, text=f"{(second_words[word_index])}", font=("", 14, "bold"),bg="cornsilk2",fg="navy")
            english_word_search.place(relx=0.5, rely=0.75, anchor="n")
        elif search_word.get() in second_words:
            word_index2 = second_words.index(search_word.get())
            german_word_search = Label(newWindow, text=f"{(first_words[word_index2])}", font=("", 14, "bold"),bg="cornsilk2",fg="midnight blue")
            german_word_search.place(relx=0.5, rely=0.75, anchor="n")
        else:
            error_search = Label(newWindow, text="Not Found", font=("", 14, "bold","italic"),bg="cornsilk2",fg="red")
            error_search.place(relx=0.5, rely=0.75, anchor="n")

    search_button = Button(newWindow, text="SEARCH", bg="olivedrab4", fg="yellow", font=("rubik", 12, "bold"),
                           activebackground="gray75", activeforeground="gold", height=1, width=10, cursor="plus",
                           relief="raised",command=sucher)
    search_button.place(relx=0.5, rely=0.6, anchor="n")


open_button = Button(tab2, text="OPEN", bg="dark olive green", fg="yellow", font=("rubik", 10, "bold"),
                     activebackground="dark green", activeforeground="orange", height=1, width=10, cursor="plus",
                     relief="raised", command=openNewWindow)
open_button.place(relx=0.45, rely=0.6, anchor="n")


# Tab 3 / drittes Fenster

title = Label(tab3, text='V-O-C-A-B-U-L-A-R-Y\nE-X-A-M', bg="navajowhite", font=("impact",50, ''))
title.place(relx=0.5, rely=0.04, anchor="n")

german_word = Label(tab3)
i = random.randint(0, len(vocabulary_entry_list) - 1)
correct = Label(tab3)
correct2 = Label(tab3)
correct3 = Label(tab3)
correct_gj = Label(tab3)
wrong = Label(tab3)
wrong2 = Label(tab3)
wrong3 = Label(tab3)
wrong4 = Label(tab3)
wrong5 = Label(tab3)


def gerword():
    global german_word
    global i
    global wrong
    global wrong2
    global wrong3
    global wrong4
    global wrong5

    english_word.delete(0, "end")

    german_word.destroy()
    correct.destroy()
    correct2.destroy()
    correct3.destroy()
    correct_gj.destroy()
    wrong.destroy()
    wrong2.destroy()
    wrong3.destroy()
    wrong4.destroy()
    wrong5.destroy()

    i = random.randint(0, len(vocabulary_entry_list) - 1)
    german_word = Label(tab3, text=f'{vocabulary_entry_list[i].german}', bg="navajowhite", font=("corbel", 16, "bold"))
    german_word.place(relx=0.5, rely=0.4, anchor="n")
    return german_word


english_word = Entry(tab3, font=12, width=22)
english_word.place(relx=0.5, rely=0.5, anchor="n")


def examine():
    global wrong
    global wrong2
    global wrong3
    global wrong4
    global wrong5
    global correct
    global correct_gj
    global english_word
    global i
    global correct2
    global correct3

    e = (english_word.get())

    if e == vocabulary_entry_list[i].english:
        correct.destroy()
        correct2.destroy()
        correct3.destroy()
        correct_gj.destroy()
        wrong.destroy()
        wrong2.destroy()
        wrong3.destroy()
        wrong4.destroy()
        wrong5.destroy()

        correct = Label(tab3, text="C O R R E C T", bg="navajowhite",fg="dark green", font=("impact", 45, ""))
        correct.place(relx=0.5, rely=0.61, anchor="n")

        correct_gj = Label(tab3, text="Good Job!", bg="navajowhite", fg="forest green", font=("impact", 16, ""))
        correct_gj.place(relx=0.5, rely=0.74, anchor="n")

        correct2 = Label(tab3, text=f"{vocabulary_entry_list[i].example}", width=100,bg="navajowhite",font=("corbel", 13, "italic"))
        correct2.place(relx=0.5, rely=0.82, anchor="n")

        correct3 = Label(tab3, text="Example:", bg="navajowhite",font=("corbel", 13, "bold"))
        correct3.place(relx=0.2, rely=0.82, anchor="n")
    else:
        correct.destroy()
        correct2.destroy()
        correct3.destroy()
        correct_gj.destroy()
        wrong.destroy()
        wrong2.destroy()
        wrong3.destroy()
        wrong4.destroy()
        wrong5.destroy()

        wrong = Label(tab3, text="W R O N G", bg="navajowhite",fg="red", font=("impact",40, ""))
        wrong.place(relx=0.5, rely=0.60, anchor="n")

        wrong2 = Label(tab3, text="The correct word is:",bg="navajowhite", font=("comic sans ms", 13, ""))
        wrong2.place(relx=0.5, rely=0.73, anchor="n")

        wrong3 = Label(tab3, text=f"{vocabulary_entry_list[i].english}", bg="navajowhite",fg="dark green", font=("corbel", 16, "bold"))
        wrong3.place(relx=0.5, rely=0.78, anchor="n")

        wrong4 = Label(tab3, text=f"{vocabulary_entry_list[i].example}", width=100,bg="navajowhite",font=("corbel", 13, "italic"))
        wrong4.place(relx=0.5, rely=0.86, anchor="n")

        wrong5 = Label(tab3, text="Example:", bg="navajowhite",font=("corbel", 13, "bold"))
        wrong5.place(relx=0.2, rely=0.86, anchor="n")


generate_word_button = Button(tab3, text="NEW WORD", bg="dark olive green", fg="yellow", font=("rubik", 11, "bold"),
                              activebackground="dark green", activeforeground="orange", height=1, width=12, cursor="plus",
                              relief="raised", command=gerword)
generate_word_button.place(relx=0.3, rely=0.4, anchor="n")


test_button = Button(tab3, text="TEST", bg="dark olive green", fg="yellow",
                     font=("rubik", 10, "bold"),activebackground="dark green",
                     activeforeground="orange", height=1, width=12, cursor="plus",relief="raised", command=examine)
test_button.place(relx=0.3, rely=0.5, anchor="n")


tab_control.pack(expand=1, fill='both')

window.mainloop()
