class BigChar:
    def __init__(self, charname):
        self.charname = charname
        reader = open('big' + self.charname + '.txt')
        self.fontdata = reader.read()
        reader.close()

    def print(self):
        print(self.fontdata)
