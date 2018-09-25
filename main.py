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

TESTTT
"""

from tkinter import *
from random import choice

INTER_LINES = 10
SIZE_NOTE = 10

class Interface(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):

        self.SOL_KEY_NOTES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        Frame.__init__(self, fenetre, width=1000, height=500, **kwargs)
        self.pack(fill=BOTH, side="bottom")
        self.canvas = Canvas(fenetre, width=500, height=250, bg="ivory")
        # Music lines
        ligne1 = self.canvas.create_line(100, 125 - 2 * INTER_LINES, 400, 125 - 2 * INTER_LINES)
        ligne2 = self.canvas.create_line(100, 125 - INTER_LINES, 400, 125 - INTER_LINES)
        ligne3 = self.canvas.create_line(100, 125, 400, 125)
        ligne4 = self.canvas.create_line(100, 125 + INTER_LINES, 400, 125 + INTER_LINES)
        ligne5 = self.canvas.create_line(100, 125 + 2 * INTER_LINES, 400, 125 + 2 * INTER_LINES)

        noteTest = self.canvas.create_oval(125,125, 135, 135, fill="black")
        noteTest2 = self.canvas.create_oval(250, 130, 260, 140, fill="black")

        SIZE = self.canvas.create_line(0, 0, 250, 125, fill="blue")
        self.canvas.pack(side="top")

        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="right")
        self.button_start = Button(self, text="Start", command=self.cliquer)
        self.button_start.pack(side="left")

        self.Button_do = Button(self, text="Do", command=self.cliquer)
        self.Button_re = Button(self, text="Re", command=self.cliquer)
        self.Button_mi = Button(self, text="Mi", command=self.cliquer)
        self.Button_fa = Button(self, text="Fa", command=self.cliquer)
        self.Button_sol = Button(self, text="Sol", command=self.cliquer)
        self.Button_la = Button(self, text="La", command=self.cliquer)
        self.Button_si = Button(self, text="Si", command=self.cliquer)

        self.Button_do.pack(side="left")
        self.Button_re.pack(side="left")
        self.Button_mi.pack(side="left")
        self.Button_fa.pack(side="left")
        self.Button_sol.pack(side="left")
        self.Button_la.pack(side="left")
        self.Button_si.pack(side="left")


    def cliquer(self):
        """"""
        print("Selecting random note")
        noteSelection = choice(self.SOL_KEY_NOTES)
        print(noteSelection)

        self.canvas.create_oval(250, 145, 260, 155)
        self.canvas.create_oval(250, 150, 260, 160, fill="black")
        self.canvas.create_line(245, 155, 265, 155, width=2)




fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()
