import datetime


class Entry:  # This is the entry for a switcheroo

    def __init__(self, date, boxType, alternate1, alternate2, alternate3, name, phoneNumber):
        self.date = date
        self.boxType = boxType
        self.alternateList = [alternate1, alternate2, alternate3]
        self.name = name
        self.phoneNumber = phoneNumber

    def isMatch(self, entry):  # lol this isn't working. needs to check BOTH ways
        matchingOneWay = False
        for alternate in self.alternateList:
            if alternate == entry.date:
                matchingOneWay = True

        matchingOtherWay = False
        for alternate in entry.alternateList:
            if alternate == self.date:
                matchingOtherWay = True

        matchingType = self.boxType == entry.boxType

        return matchingOneWay and matchingOtherWay and matchingType


class Entries:

    entries = []

    def addEntry(self, entry):
        self.entries.append(entry)

    def readEntries(self, file):
        return

    def writeEntries(self, file):
        return

    def findMatches(self):
        matches = []
        for entry in self.entries:
            for possibleMatch in self.entries:
                if entry.isMatch(possibleMatch):
                    matches.append(entry.name + " can be matched with " + possibleMatch.name)
        return matches

if __name__ == "__main__":
    entry1 = Entry(datetime.datetime(2019, 6, 22), "Box", datetime.datetime(2019, 6, 15),
                   datetime.datetime(2019, 6, 16), datetime.datetime(2019, 6, 17), "Bob", 1111111111)

    entry2 = Entry(datetime.datetime(2019, 6, 16), "Box", datetime.datetime(2019, 6, 21),
                   datetime.datetime(2019, 6, 22), datetime.datetime(2019, 6, 24), "Mary", 2222222222)

    print(entry1.isMatch(entry2))

    entries = Entries()
    entries.addEntry(entry1)
    entries.addEntry(entry2)

    print(entries.findMatches())
