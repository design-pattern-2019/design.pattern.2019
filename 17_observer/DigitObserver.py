import time

from Observer import Observer


class DigitObserver(Observer):

    def update(self, generator):
        print('DigitObserver:' + str(generator.getNumber()))
        time.sleep(0.1)
