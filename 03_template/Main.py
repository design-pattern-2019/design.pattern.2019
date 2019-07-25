from AbstractDisplay import AbstractDisplay
from CharDisplay import CharDisplay
from StringDisplay import StringDisplay


class Main():
  d1 = CharDisplay('H')
  d1.display()
  d2 = StringDisplay('hello world')
  d2.display()
  d3 = StringDisplay('こんにちは、世界')
  d3.display()


if __name__ == "__main__":
  Main