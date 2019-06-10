"""
This is the main window for the project. It has all the GUI components.
I might just start testing without GUI first though!!

"""

import tkinter as tk
from tkinter import ttk
from classes import *


class MainWindow(tk.Tk):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry("800x600")
        self.title("Switcheroo List")
        entry1 = Entry(datetime.datetime(2019, 6, 22), "Box", datetime.datetime(2019, 6, 15),
                       datetime.datetime(2019, 6, 16), datetime.datetime(2019, 6, 17), "Bob", 1111111111)
        self.displayEntry(entry1, 0)

    def displayEntry(self, entry, row):
        resultsLabel = tk.Label(self, text=entry.name, font="Arial 11 bold", fg="black", borderwidth=5, bg="salmon")
        resultsLabel.grid(column=1, row=row)

if __name__ == "__main__":
    switcheroo = MainWindow()
    switcheroo.mainloop()

