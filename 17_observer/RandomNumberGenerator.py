import random

from NumberGenerator import NumberGenerator


class RandomNumberGenerator(NumberGenerator):
    def getNumber(self):
        return self.number

    def execute(self):
        for i in range(20):
            self.number = random.randint(0, 49)
            self.notifyObervers()
