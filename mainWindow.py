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


    def displayEntry(self, entry, row):
        entryLabel = tk.Label(self, text=entry.name, font="Arial 11 bold", fg="black", borderwidth=5, bg="salmon")
        entryLabel.grid(column=1, row=row)

    def loadEntries(self, entries):
        row = 0
        for entry in entries.entries:
            self.displayEntry(entry, row)
            print(entry.name)
            row += 1


if __name__ == "__main__":
    switcheroo = MainWindow()

    entry1 = Entry(datetime.datetime(2019, 6, 22), "Box", datetime.datetime(2019, 6, 15),
                   datetime.datetime(2019, 6, 16), datetime.datetime(2019, 6, 17), "Bob", 1111111111)

    entry2 = Entry(datetime.datetime(2019, 6, 16), "Box", datetime.datetime(2019, 6, 21),
                   datetime.datetime(2019, 6, 22), datetime.datetime(2019, 6, 24), "Mary", 2222222222)

    testEntries = Entries()

    testEntries.addEntry(entry1)
    testEntries.addEntry(entry2)
    print(testEntries.entries)

    switcheroo.loadEntries(testEntries)

    switcheroo.mainloop()
