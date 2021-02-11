from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import random


window = Tk()

window.title("Vokabeltrainer")
window.geometry('1100x700')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control, style='new.TFrame')
tab2 = ttk.Frame(tab_control, style='new.TFrame')
tab3 = ttk.Frame(tab_control, style='new.TFrame')

s = ttk.Style()
s.configure('new.TFrame', background='navajowhite')

tab_control.add(tab1, text='Home')
tab_control.add(tab2, text='Vokabel')
tab_control.add(tab3, text='Test')


# Tab 1 : erstes Fenster

def Willkommen():
    x1, y1, x2, y2 = canvas.bbox("marquee")
    if (x2 < 0 or y1 < 0):
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height() // 2
        canvas.coords("marquee", x1, y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000 // fps, Willkommen)


canvas = Canvas(tab1, bg='bisque')
canvas.pack(anchor=N, expand=1, pady=40)
text_var = "WILLKOMMEN ZUM VOKABELTRAINER!!!"
text = canvas.create_text(0, -2000, text=text_var, font=('comic sans ms', 26, 'bold'), fill='dark olive green',tags=("marquee",), anchor='w')
x1, y1, x2, y2 = canvas.bbox("marquee")
canvas['width'] = 550
canvas['height'] = 64
fps = 80  # Schnelligkeit der Animation einstellen
Willkommen()


beschreibung = Label(tab1, text="""Beschreibung:\n
Das ist ein Vokabeltrainer mit einer integrierten Vokabelliste\nindem du Fremdwoerter, deren Uebersetzung und Beispielsaetze findest."\n
Tab "Vokabel": - lerne alle Vokabel und fuege neue hinzu!\nTab "Test": - führe den Vokabeltest durch\n um deine Sprachfaehigkeiten auf die Probe zu stellen!""",
             bg="bisque", padx=20, pady=20, font=("comic sans ms", 13, ""))
beschreibung.place(relx=0.5, rely=0.25, anchor="n")

viel_spass = Label(tab1, text="Viel Spaß!", bg="navajowhite", font=("comic sans ms", 22, "bold"), fg="dark olive green")
viel_spass.place(relx=0.5, rely=0.63, anchor="n")

regeln = Label(tab1, text="""Regeln:\n
"ü" = "ue"\n"ä" = "ae"\n"ö" = "oe"\n"ß" = "ss" """,bg="navajowhite",
             font=("corbel", 13, "bold"))
regeln.place(relx=0.5, rely=0.72, anchor="n")

made_by = Label(tab1, text="@Developed by Angel Mechkarov", bg="navajowhite", font=("Miriam Mono CLM", 11, ""),
             fg="gray30")
made_by.place(relx=0.5, rely=0.94, anchor="n")


class VOKABEL:
    def __init__(self, englisch, deutsch, beispiel):
        self.englisch = englisch
        self.deutsch = deutsch
        self.beispiel = beispiel

    def zeile(self):
        treev.insert("", "end", text="L1",
                     values=(self.englisch, self.deutsch, self.beispiel))


eintraege = []

datei = "./vocabulary.txt"
if os.path.isfile(datei):
    vokabelwoerter = open(datei)

    for line in vokabelwoerter:
        vokabelwoerter = line.split(",")
        eintraege.append(VOKABEL(vokabelwoerter[0].strip(), vokabelwoerter[1].strip(),vokabelwoerter[2].strip()))


#Tab 2 / zweites Fenster
#Die Vokabelliste mit 'Treeview' erstellen

treev = ttk.Treeview(tab2, selectmode='browse')
treev.pack(side='top', ipady="80")

scrlbar = ttk.Scrollbar(tab2, orient="vertical", command=treev.yview)

scrlbar.place(relx=0.10, rely=0.01, anchor="n", height=370)

treev.configure(xscrollcommand=scrlbar.set)

treev["columns"] = ("1", "2", "3")
treev['show'] = 'headings'

treev.column("1", width=170, anchor='center')
treev.column("2", width=170, anchor='center')
treev.column("3", width=120, anchor='center')

treev.heading("1", text="Englisch")
treev.heading("2", text="Deutsch")
treev.heading("3", text="Beispiel")

treev.column('1', stretch=tk.YES)
treev.column('2', stretch=tk.YES)
treev.column('3', width="500")


for eintrag in eintraege:
    print(eintrag.zeile())


entry_englisch = Entry(tab2, font=12, width=25)
entry_englisch.place(relx=0.43, rely=0.71, anchor="n")

entry_deutsch = Entry(tab2, font=12, width=25)
entry_deutsch.place(relx=0.43, rely=0.81, anchor="n")

entry_beispiel = Entry(tab2, font=12, width=40)
entry_beispiel.place(relx=0.49, rely=0.91, anchor="n")


label_englisch = Label(tab2, text="Englisches Wort:", bg="navajowhite", font=("corbel", 13, "bold"))
label_englisch.place(relx=0.23, rely=0.71, anchor="n")

label_deutsch = Label(tab2, text="Deutsches Wort:", bg="navajowhite", font=("corbel", 13, "bold"))
label_deutsch.place(relx=0.23, rely=0.81, anchor="n")

label_beispiel = Label(tab2, text="Beispiel:", bg="navajowhite", font=("corbel", 13, "bold"))
label_beispiel.place(relx=0.23, rely=0.91, anchor="n")


#Liste: erstes Wort in jeder Zeile (Englisches Wort)
with open(datei,"r") as f:
    first_words = [line.split(",",maxsplit=1)[0] for line in f if line.strip()]
#print(first_words)

#Liste: zweites Wort in jeder Zeile (Deutsches Wort)
with open(datei,"r") as f:
    second_words = [line.split(",",maxsplit=2)[1] for line in f if line.strip()]
#print(second_words)


#Filter: englische Woerter die schon existieren => erzeugen ein "Error!"

existing_word = Label(tab2)


def speichern():
    global existing_word

    existing_word.destroy()

    if entry_englisch.get() in first_words:
        existing_word = Label(tab2,text="Error: Wort existiert bereits!",font=("corbel",14,"bold"),bg="navajowhite",fg="red")
        existing_word.place(relx=0.8,rely=0.9,anchor="n")
    else:
        treev.insert("", "end", text="L1",
                     values=(entry_englisch.get(), entry_deutsch.get(), entry_beispiel.get()))

        with open(datei, "a+") as save_words:
            save_words.write(f"\n{entry_englisch.get()},{entry_deutsch.get()},{entry_beispiel.get()}")

        entry_englisch.delete(0, END)
        entry_deutsch.delete(0, END)
        entry_beispiel.delete(0, END)


def entfernen():
    x = treev.selection()[0]
    treev.delete(x)


save_button = Button(tab2, text="SPEICHERN", bg="dark olive green", fg="yellow", font=("rubik", 13, "bold"),
                     activebackground="dark green", activeforeground="orange", height=1, width=10, cursor="plus",
                     relief="raised", command=speichern)
save_button.place(relx=0.65, rely=0.71, anchor="n")

delete_button = Button(tab2, text="ENTFERNEN", bg="dark olive green", fg="yellow", font=("rubik", 10, "bold"),
                       activebackground="dark green", activeforeground="orange", height=1, width=10, cursor="plus",
                       relief="raised", command=entfernen)
delete_button.place(relx=0.65, rely=0.81, anchor="n")


info_save = Label(tab2,text='*INFO!*\n Klicke auf "SPEICHERN" um das \neingegebene DEU/ENG-Wort in der Tabelle\n zu speichern!',
                  bg="navajowhite", font=("corbel", 8, ""))
info_save.place(relx=0.84, rely=0.69, anchor="n")

info_delete = Label(tab2,text='*INFO!*\n Klicke auf ein Wort in der Tabelle\n und klicke dann auf "ENTFERNEN" um dieses\n aus der Tabelle zu loeschen!',
                    bg="navajowhite", font=("corbel", 8, ""))
info_delete.place(relx=0.84, rely=0.79, anchor="n")

search_open_text = Label(tab2, text='Nach Woertern aus der Tabelle suchen:', bg="navajowhite", font=("corbel", 13, "italic"))
search_open_text.place(relx=0.3, rely=0.6, anchor="n")


def openNewWindow():
    newWindow = Toplevel(tab2,bg="cornsilk2")
    newWindow.title("Suchmaschine")
    newWindow.geometry("350x350")

    search_text = Label(newWindow, text="Suche ein Wort",bg="cornsilk2",fg="dark olive green",font=("", 14, "bold"))
    search_text.place(relx=0.5, rely=0.03, anchor="n")

    description_search = Label(newWindow, text="Gib ein Wort ein\n um die Uebersetzung zu erhalten", bg="cornsilk2",fg="black", font=("", 10, "bold"))
    description_search.place(relx=0.5, rely=0.18, anchor="n")

    give_word_text = Label(newWindow, text="Wort:", bg="cornsilk2",fg="black", font=("", 10, "bold"))
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
            error_search = Label(newWindow, text="NOT FOUND", font=("", 14, "bold"),bg="cornsilk2",fg="red")
            error_search.place(relx=0.5, rely=0.75, anchor="n")

    search_button = Button(newWindow, text="SUCHEN", bg="olivedrab4", fg="yellow", font=("rubik", 10, "bold"),
                   activebackground="gray75", activeforeground="gold", height=1, width=10, cursor="plus",
                   relief="raised",command=sucher)
    search_button.place(relx=0.5, rely=0.6, anchor="n")


open_button = Button(tab2, text="OPEN", bg="dark olive green", fg="yellow", font=("rubik", 10, "bold"),
               activebackground="dark green", activeforeground="orange", height=1, width=10, cursor="plus",
               relief="raised", command=openNewWindow)
open_button.place(relx=0.48, rely=0.6, anchor="n")


# Tab 3 / drittes Fenster

title = Label(tab3, text='V-O-K-A-B-E-L-T-E-S-T', bg="navajowhite", font=("impact", 50, ''))
title.place(relx=0.5, rely=0.04, anchor="n")

ger_word = Label(tab3)
i = random.randint(0, len(eintraege) - 1)
correct = Label(tab3)
correct2 = Label(tab3)
correct3 = Label(tab3)
wrong = Label(tab3)
wrong2 = Label(tab3)
wrong3 = Label(tab3)
wrong4 = Label(tab3)
wrong5 = Label(tab3)


def gerword():
    global ger_word
    global i
    global wrong
    global wrong2
    global wrong3
    global wrong4
    global wrong5

    english_word.delete(0, "end")

    ger_word.destroy()
    correct.destroy()
    correct2.destroy()
    correct3.destroy()
    wrong.destroy()
    wrong2.destroy()
    wrong3.destroy()
    wrong4.destroy()
    wrong5.destroy()

    i = random.randint(0, len(eintraege) - 1)
    ger_word = Label(tab3, text=f'{eintraege[i].deutsch}', bg="navajowhite", font=("corbel", 16, "bold"))
    ger_word.place(relx=0.5, rely=0.3, anchor="n")
    return ger_word


english_word = Entry(tab3, font=12, width=22)
english_word.place(relx=0.5, rely=0.44, anchor="n")


def pruefen():
    global wrong
    global wrong2
    global wrong3
    global wrong4
    global wrong5
    global correct
    global english_word
    global i
    global correct2
    global correct3

    e = (engl_word.get())

    if e == eintraege[i].englisch:
        correct.destroy()
        correct2.destroy()
        correct3.destroy()
        wrong.destroy()
        wrong2.destroy()
        wrong3.destroy()
        wrong4.destroy()
        wrong5.destroy()

        correct = Label(tab3, text="K O R R E K T !", bg="navajowhite",fg="dark green", font=("impact", 38, ""))
        correct.place(relx=0.5, rely=0.65, anchor="n")

        correct2 = Label(tab3, text=f"{eintraege[i].beispiel}", width=100,bg="navajowhite",font=("corbel", 13, "italic"))
        correct2.place(relx=0.5, rely=0.77, anchor="n")

        correct3 = Label(tab3, text="Beispiel:", bg="navajowhite",font=("corbel", 13, "bold"))
        correct3.place(relx=0.2, rely=0.77, anchor="n")
    else:
        correct.destroy()
        correct2.destroy()
        correct3.destroy()
        wrong.destroy()
        wrong2.destroy()
        wrong3.destroy()
        wrong4.destroy()
        wrong5.destroy()

        wrong = Label(tab3, text="F A L S C H !", bg="navajowhite",fg="red", font=("impact", 34, ""))
        wrong.place(relx=0.5, rely=0.62, anchor="n")

        wrong2 = Label(tab3, text="Das richtige Wort lautet:",bg="navajowhite", font=("corbel", 12, "bold"))
        wrong2.place(relx=0.5, rely=0.75, anchor="n")

        wrong3 = Label(tab3, text=f"{eintraege[i].englisch}", bg="navajowhite",fg="dark green", font=("corbel", 16, "bold"))
        wrong3.place(relx=0.5, rely=0.8, anchor="n")

        wrong4 = Label(tab3, text=f"{eintraege[i].beispiel}", width=100,bg="navajowhite",font=("corbel", 13, "italic"))
        wrong4.place(relx=0.5, rely=0.86, anchor="n")

        wrong5 = Label(tab3, text="Beispiel:", bg="navajowhite",font=("corbel", 13, "bold"))
        wrong5.place(relx=0.2, rely=0.86, anchor="n")


generate_word_button = Button(tab3, text="NEUES WORT", bg="dark olive green", fg="yellow", font=("rubik", 11, "bold"),
                              activebackground="dark green", activeforeground="orange", height=1, width=12, cursor="plus",
                              relief="raised", command=gerword)
generate_word_button.place(relx=0.3, rely=0.3, anchor="n")


test_button = Button(tab3, text="TEST", bg="dark olive green", fg="yellow",
                     font=("rubik", 11, "bold"),activebackground="dark green",
                     activeforeground="orange", height=1, width=12, cursor="plus",relief="raised", command=pruefen)
test_button.place(relx=0.5, rely=0.5, anchor="n")


tab_control.pack(expand=1, fill='both')

window.mainloop()
