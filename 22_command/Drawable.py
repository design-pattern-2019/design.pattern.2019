from abc import ABCMeta, abstractmethod

class Drawable(metaclass=ABCMeta):
    @abstractmethod
    def draw(x: int, y: int) -> None:
        pass
