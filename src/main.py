"""
Maximilien
Romain
2018

This software is a simple program that helps the user to train reading music sheet

Do  -   Re  -   Mi   -  Fa   -  Sol  -  La   -  Si   -  Do
1       2       3       4       5       6       7       8

***** Sol key *****
                     Sol
-------------------Fa--------------------
                 Mi
---------------Re------------------------
             Do
-----------Si----------------------------
         La
------Sol--------------------------------
    Fa
--Mi-------------------------------------
RE


"""
#TODO: Adding FA Key and porte below SOL and not under
#TODO: Remove start button, play directly

from tkinter import *
from tkinter import messagebox

from random import choice
from PIL import Image, ImageTk


INTER_LINES = 10
DIFFERENTIAL_NOTE = INTER_LINES / 2
SIZE_NOTE = INTER_LINES

class Interface(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):

        self.SOL_KEY_NOTES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.randomNote = 0
        self.score = 0
        self.totalNote = 0
        self.started = False

        Frame.__init__(self, fenetre, width=1000, height=500, **kwargs)
        self.pack(fill=BOTH, side="bottom")
        self.canvas = Canvas(fenetre, width=500, height=250, bg="ivory")
        # Music lines
        ligne1 = self.canvas.create_line(100, 125 - 2 * INTER_LINES, 400, 125 - 2 * INTER_LINES)
        ligne2 = self.canvas.create_line(100, 125 - INTER_LINES, 400, 125 - INTER_LINES)
        ligne3 = self.canvas.create_line(100, 125, 400, 125)
        ligne4 = self.canvas.create_line(100, 125 + INTER_LINES, 400, 125 + INTER_LINES)
        ligne5 = self.canvas.create_line(100, 125 + 2 * INTER_LINES, 400, 125 + 2 * INTER_LINES)

        self.baseNote = self.canvas.create_oval(250, 150, 260, 160, fill="black")

        self.canvas.pack(side="top")

        image = PhotoImage(file="../fig/sol.gif")
        image = image.subsample(15)
        self.canvas.create_image(110, 170, image=image, anchor=S)
        label = Label(image=image)
        label.image = image # keep a reference!

        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="right")
        self.button_start = Button(self, text="Start", command=self.start)
        self.button_start.pack(side="left")

        self.Button_do = Button(self, text="Do", command=self.doSelection)
        self.Button_re = Button(self, text="Re", command=self.reSelection)
        self.Button_mi = Button(self, text="Mi", command=self.miSelection)
        self.Button_fa = Button(self, text="Fa", command=self.faSelection)
        self.Button_sol = Button(self, text="Sol", command=self.solSelection)
        self.Button_la = Button(self, text="La", command=self.laSelection)
        self.Button_si = Button(self, text="Si", command=self.siSelection)

        self.Button_do.pack(side="left")
        self.Button_re.pack(side="left")
        self.Button_mi.pack(side="left")
        self.Button_fa.pack(side="left")
        self.Button_sol.pack(side="left")
        self.Button_la.pack(side="left")
        self.Button_si.pack(side="left")


    def start(self):
        self.randomNote = choice(self.SOL_KEY_NOTES)
        self.noteLine = None
        self.started = True
        self.noteLines = []

        # First note in SOL KEY
        #self.canvas.create_oval(250, 150, 260, 160, fill="black")
        #self.canvas.create_line(245, 155, 265, 155, width=2)

        # ***** Scoring labels *****
        goodNoteScoreText = "Score {0}/{1}".format(self.score, self.totalNote)
        badNoteScoreText = "Wrong note {0}/{1}".format((self.totalNote - self.score), self.totalNote)
        self.scoreItem = self.canvas.create_text(50, 20, text=goodNoteScoreText)
        self.wrongNoteScoreItem = self.canvas.create_text(150, 20, text=badNoteScoreText)

        self.canvas.coords(self.baseNote, 250, 150 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), 260, 160 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE))

    def gameLoop(self):
        self.cleanLines()
        self.randomNote = choice(self.SOL_KEY_NOTES)

        goodNoteScoreText = "Score {0}/{1}".format(self.score, self.totalNote)
        badNoteScoreText = "Wrong note {0}/{1}".format((self.totalNote - self.score), self.totalNote)
        self.canvas.delete(self.scoreItem)
        self.canvas.delete(self.wrongNoteScoreItem)
        self.scoreItem = self.canvas.create_text(50, 20, text=goodNoteScoreText, fill="green")
        self.wrongNoteScoreItem = self.canvas.create_text(150, 20, text=badNoteScoreText, fill="red")

        # First Do need line on the note

        if self.randomNote == 1:
            noteLine = self.canvas.create_line(245, 155, 265, 155, width=2)
            self.noteLines += [noteLine]
        elif self.randomNote ==  13: # La
            noteLine = self.canvas.create_line(245, 155 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), 265, 155 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), width=2)
            self.noteLines += [noteLine]
        elif self.randomNote == 14: # Si
            noteLine = self.canvas.create_line(245, 160 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), 265, 160 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), width=2)
            self.noteLines += [noteLine]
        elif self.randomNote == 15: # Do
            line1 = self.canvas.create_line(245, 155 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), 265, 155 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), width=2)
            line2 = self.canvas.create_line(245, 165 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), 265, 165 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), width=2)
            self.noteLines += [line1]
            self.noteLines += [line2]

        self.canvas.coords(self.baseNote, 250, 150 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE), 260, 160 - ((self.randomNote - 1) * DIFFERENTIAL_NOTE))

    def noteSelection(self, selectedNote):
        """ Verification of random note for notes selection """
        if not self.started:
            messagebox.showwarning("Warning", "Please press START")
        else:
            print(selectedNote)
            if self.randomNote in [selectedNote, selectedNote + 7, selectedNote + 2*7]:
                self.score += 1
                print("Find good note")
            else:
                print("Wrong note")
            self.totalNote += 1
            self.gameLoop()

    def cleanLines(self):
        for elem in self.noteLines:
            self.canvas.delete(elem)
        self.noteLines = []

    def doSelection(self):
        """ Do Button selected """
        self.noteSelection(1)

    def reSelection(self):
        """ Re Button selected """
        self.noteSelection(2)

    def miSelection(self):
        """ Mi Button selected """
        self.noteSelection(3)

    def faSelection(self):
        """ Fa Button selected """
        self.noteSelection(4)

    def solSelection(self):
        """ Sol Button selected """
        self.noteSelection(5)

    def laSelection(self):
        """ La Button selected """
        self.noteSelection(6)

    def siSelection(self):
        """ Si Button selected """
        self.noteSelection(7)


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
