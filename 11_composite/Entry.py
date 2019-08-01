from abc import ABCMeta, abstractmethod

from FileTreatmentException import FileTreatmentException


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getSize(self):
        pass

    def add(self, entry):
        raise FileTreatmentException()

    @abstractmethod
    def printList(self, prefix):
        pass

    def __str__(self):
        return self.getName() + " (" + str(self.getSize()) + ")"
