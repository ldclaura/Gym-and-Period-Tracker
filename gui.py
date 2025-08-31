from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.config(padx=100, pady=50, bg="#f7f5dd")
        self.canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)

        #GRID
        self.canvas1 = Canvas(width=200, height=200, bg=RED, highlightthickness=0)
        self.canvas1 = Entry()
        self.canvas1.grid(column=1, row=1, columnspan=3)

        self.canvas2 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas2.grid(column=1, row=2)

        self.canvas3 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas3.grid(column=1, row=3)

        self.canvas4 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas4.grid(column=2, row=1)

        self.canvas5 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas5.grid(column=2, row=2)

        self.canvas6 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas6.grid(column=2, row=3)

        self.canvas7 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas7.grid(column=3, row=1)

        self.canvas8 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas8.grid(column=3, row=2)

        self.canvas9 = Canvas(width=200, height=200, highlightthickness=0)
        self.canvas9.grid(column=3, row=3)

        self.canvas1 = Canvas(width=200, height=200, bg=RED, highlightthickness=0)
        self.canvas1 = Entry()
        self.canvas1.grid(column=1, row=1, columnspan=3)



start = GUI()
start.mainloop()