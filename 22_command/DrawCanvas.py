from Command import Command
from MacroCommand import MacroCommand
from Drawable import Drawable
from tkinter import *

class DrawCanvas(Canvas, Drawable):
    def __init__(self, parent, width: int, height: int, history: MacroCommand):
        # Canvasの初期化
        Canvas.__init__(self, parent, width=width, height=height, bg="#fff")
        self.__color = '#f00'
        self.__radius = 6
        self.__history = history

    def repaint(self) -> None:
        self.delete("all")
        self.__history.execute()

    def draw(self, x: int, y: int) -> None:
        # 面積 radius * 2 * 3.14 の円を作る
        self.create_oval(
            x - self.__radius, y - self.__radius,
            x + self.__radius, y + self.__radius,
            fill=self.__color,
            outline=""
        )
