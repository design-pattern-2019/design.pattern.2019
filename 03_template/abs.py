from abc import ABCMeta, abstractmethod


class Abs(metaclass=ABCMeta):
  @abstractmethod
  def open(self):
    pass

  @abstractmethod
  def print(self):
    pass

  @abstractmethod
  def close(self):
    pass

  def display(self):
    self.open()
    for _ in range(5):
      self.print()
    self.close()
    print()