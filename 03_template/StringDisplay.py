from AbstractDisplay import AbstractDisplay


class StringDisplay(AbstractDisplay):
  def __init__(self, string):
    self.string = string
    self.width = sum([len(str(ord(_))) // 2 for _ in string])

  def printLine(self):
    print("+", end='')
    for _ in range(self.width):
      print("_", end='')
    print("+", end='')

  def open(self):
    self.printLine()
    print()

  def print(self):
    print("|" + self.string + "|")

  def close(self):
    self.printLine()