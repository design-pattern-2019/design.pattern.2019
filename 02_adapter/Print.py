from abc import ABCMeta, abstractmethod

class Print(metaclass=ABCMeta):
    @abstractmethod
    def printWeek():
        pass

    def printStrong():
        pass
