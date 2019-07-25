class AbstractDisplay:
  def output(self):
    self.open()
    self.print()
    self.close()

  def open(self):
    pass

  def print(self):
    pass

  def close(self):
    pass

  def display(self):
    self.open()
    for _ in range(5):
      self.print()
    self.close()
  # 行を整える
    print()