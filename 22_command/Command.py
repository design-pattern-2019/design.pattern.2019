from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute() -> None:
        pass
