from Command import Command
from Drawable import Drawable
from Point import Point

class DrawCommand(Command):
    def __init__(self, drawable: Drawable, position: Point):
        self.drawable = drawable
        self.position = position

    def execute(self) -> None:
        self.drawable.draw(self.position.x, self.position.y)

