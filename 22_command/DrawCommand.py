from Command import Command
from Drawable import Drawable
from Point import Point

class DrawCommand(Command):
    def __init__(self, drawable: Drawable, position: Point):
        self._drawable = drawable
        self.__position = position

    def execute(self) -> None:
        self._drawable.draw(self.__position.x, self.__position.y)

