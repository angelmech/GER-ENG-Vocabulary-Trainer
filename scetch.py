import random
import os

class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch

    def zeile(self):
        return self.deutsch + " - " + self.englisch

eintraege = []

datei = "./vokabel.txt"
if os.path.isfile(datei):
    vokabelwoerter = open(datei)

    for line in vokabelwoerter:
        vokabelwoerter = line.split(",")
        eintraege.append(Entry(vokabelwoerter[0].strip(), vokabelwoerter[1].strip()))


def eingabe():
    while True:
        deutsch = input("Deutsches Wort: ")
        if deutsch == "#":
            return
        englisch = input("Englisches Wort: ")
        if englisch == "#":
            return
        eintraege.append(Entry(deutsch, englisch))
        with open(datei,"a+") as save_words:
            save_words.write(f"\n{deutsch},{englisch}")


def test():
    while True:
        i = random.randint(0, len(eintraege) - 1)
        englisch = input("\nEnglische Übersetzung von " + eintraege[i].deutsch + ": ")
        if (englisch == "#"):
            return
        if eintraege[i].englisch == englisch:
            print("Korrekt!")
        else:
            print("Falsch! | Die Richtige Antwort: " + eintraege[i].englisch)


def show_all():
    for eintrag in eintraege:
        print(eintrag.zeile())


while True:
    print("\n----- VOKABELTRAINER -----\n")
    befehl = input("""Optionsmenu:
     Wörterbuch erweitern:      "add"
     Wörterbuch anzeigen:       "list"
     Vokabeltest:               "test"
     Programm schließen:        "end"
     > Hier Befehl eintippen: """)
    if befehl == "add":
        print("\n*(Tippe '#' um zum Optionsmenu zurückzukehren) *")
        eingabe()
    elif befehl == "test":
        print("\n*(Tippe '#' um zum Optionsmenu zurückzukehren) *")
        test()
    elif befehl == "end":
        print(8*"-","ENDE",8*"-")
        break
    elif befehl == "list":
        show_all()
    else:
        print("\nERROR! Kein gültiger Befehl.")
