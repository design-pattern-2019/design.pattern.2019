from abc import ABCMeta, abstractmethod
from Context import Context

class Node(metaclass=ABCMeta):
    @abstractmethod
    def parse(context: Context):
        pass
