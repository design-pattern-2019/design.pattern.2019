from abc import ABCMeta, abstractmethod
import copy


class Product(metaclass=ABCMeta):
  @abstractmethod
  def use(self, s):
    pass

  def createClone(self):
    return copy.deepcopy(self)