from Banner import Banner
from Print import Print

class PrintBanner(Banner, Print):
    def __init__(self, string):
        super().__init__(string)

    def printWeek(self):
        super().showWithParen()

    def printStrong(self):
        super().showWithAster()
