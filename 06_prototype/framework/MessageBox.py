from framework.Product import Product
import unicodedata


class MessageBox(Product):
  def __init__(self, decochar):
    self.decochar = decochar

  def use(self, s):
    length = self.count_chara(s)

    for _ in range(length + 4):
      print(self.decochar, end='')
    print()

    print(self.decochar + ' ' + s + ' ' + self.decochar)

    for _ in range(length + 4):
      print(self.decochar, end='')
    print()

  def count_chara(self, cha):
    length = 0
    for c in cha:
        if unicodedata.east_asian_width(c) in ['W', 'W']:
            length += 2
        else:
            length += 1

    return length
