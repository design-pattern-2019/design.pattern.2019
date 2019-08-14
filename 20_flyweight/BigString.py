from BigCharFactory import BigCharFactory


class BigString:
    def __init__(self, string):
        self.bigchars = []
        self.factory = BigCharFactory.getInstance()
        for c in string:
            self.bigchars.append(self.factory.getBigChar(c))

    def print(self):
        for c in self.bigchars:
            c.print()
