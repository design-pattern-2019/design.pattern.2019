import time

from Observer import Observer


class GraphObserver(Observer):

    def update(self, generator):
        print('GraphObserver:', end='')
        time.sleep(0.1)
        count = generator.getNumber()
        print('*' * count)
        time.sleep(0.1)
