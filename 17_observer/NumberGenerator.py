from abc import ABCMeta, abstractmethod


class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def deleteObserver(self, observer):
        self.observers.remove(observer)

    def notifyObervers(self):
        for o in self.observers:
            o.update(self)

    @abstractmethod
    def getNumber(self):
        pass

    @abstractmethod
    def execute(self):
        pass
