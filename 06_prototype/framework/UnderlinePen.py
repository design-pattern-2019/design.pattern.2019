from framework.Product import Product
import unicodedata

class UnderlinePen(Product):
  def __init__(self, ulchar):
    self.ulchar = ulchar

  def use(self, s):
    length = self.count_chara(s)

    print(self.ulchar + s + self.ulchar)

    for _ in range(length + 4):
      print(self.ulchar, end='')
    print()

  def count_chara(self, cha):
    length = 0
    for c in cha:
        if unicodedata.east_asian_width(c) in ['W', 'W']:
            length += 2
        else:
            length += 1

    return length


