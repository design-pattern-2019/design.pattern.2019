from Command import Command
from MacroCommand import MacroCommand
from Drawable import Drawable
from tkinter import *

# Test用
from Point import Point
from DrawCommand import DrawCommand

class DrawCanvas(Canvas, Drawable):
    def __init__(self, parent, width: int, height: int, history: MacroCommand):
        # Canvasの初期化
        Canvas.__init__(self, parent, width=width, height=height, bg="#fff")
        self.color = '#f00'
        self.radius = 6
        self.history = history

    def paint(self) -> None:
        self.history.execute()

    def draw(self, x: int, y: int) -> None:
        # 面積 radius * 2 * 3.14 の円を作る
        self.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius, fill=self.color, outline="")
