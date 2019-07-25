from AbstractDisplay import AbstractDisplay

class CharDisplay(AbstractDisplay):
  def __init__(self, chr):
    self.chr = chr

  def open(self):
    print("<<", end='')

  def print(self):
    print(self.chr, end='')

  def close(self):
    print(">>", end='')