from Entry import Entry


class Directory(Entry):

    def __init__(self, name):
        self.name = name
        self.directory = []

    def getName(self):
        return self.name

    def getSize(self):
        size = 0
        for i in self.directory:
            size += i.getSize()
        return size

    def add(self, entry):
        self.directory.append(entry)
        return self.directory

    def printList(self, prefix=''):
        print(prefix + "/" + str(self))
        for i in self.directory:
            i.printList(prefix + "/" + self.name)
