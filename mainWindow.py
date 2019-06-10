"""
This is the main window for the project. It has all the GUI components.
I might just start testing without GUI first though!!

"""

import tkinter as tk
import datetime


class Entry:  # This is the entry for a switcheroo

    def __init__(self, date, boxType, alternate1, alternate2, alternate3, name, phoneNumber):
        self.date = date
        self.boxType = boxType
        self.alternateList = [alternate1, alternate2, alternate3]
        self.name = name
        self.phoneNumber = phoneNumber

    def isMatch(self, entry):
        matchingDates = False
        for alternate in self.alternateList:
            if alternate == entry.date:
                matchingDates = True
        matchingType = self.boxType == entry.boxType
        return matchingDates and matchingType


class MainWindow:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Switcheroo List")

    def run(self):
        self.mainWin.mainloop()


if __name__ == "__main__":
    switeroo = MainWindow()
    # switeroo.run()

    entry1 = Entry(datetime.datetime(2019, 6, 23), "Box", datetime.datetime(2019, 6, 15),
                   datetime.datetime(2019, 6, 16), datetime.datetime(2019, 6, 17), "Bob", 1111111111)
    entry2 = Entry(datetime.datetime(2019, 6, 16), "Box", datetime.datetime(2019, 6, 21),
                   datetime.datetime(2019, 6, 22), datetime.datetime(2019, 6, 23), "Mary", 1111111111)

    print(entry1.isMatch(entry2))