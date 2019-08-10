from tkinter import *
from MacroCommand import MacroCommand
from DrawCommand import DrawCommand
from DrawCanvas import DrawCanvas
from Drawable import Drawable
from Point import Point

class Main(Tk):
    def __init__(self, title: str):
        Tk.__init__(self)
        self.title(title)

        # ボックスを作成
        mainBox = Frame(self)
        mainBox.pack()
        buttonBox = Frame(mainBox)
        buttonBox.pack()

        # プロパティ初期化
        self.__history = MacroCommand()
        self.__canvas = DrawCanvas(mainBox, 400, 400, self.__history)
        self.__canvas.pack()
        self.__button = Button(buttonBox, text="Clear")
        self.__button.pack()

        # 操作系の設定
        self.__canvas.bind("<B1-Motion>", self.mouseMoveWithHoldDownRightClick)
        self.__button.bind("<1>", self.onClickClearButton)

        self.mainloop()

    def mouseMoveWithHoldDownRightClick(self, e) -> None:
        cmd = DrawCommand(self.__canvas, Point(e.x, e.y))
        self.__history.append(cmd)
        cmd.execute()

    def onClickClearButton(self, e) -> None:
        self.__history.clear()
        self.__canvas.delete("all")

if __name__ == '__main__':
    Main("お絵かき")
