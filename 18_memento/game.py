import copy
import random


class Memento:
    def __init__(self, money):
        self.money = money
        self.fruits = []

    def getMoney(self):
        return self.money

    def addFruit(self, fruit):
        self.fruits.append(fruit)

    def getFruits(self):
        return copy.copy(self.fruits)


class Gamer:
    fruitsname = [
        'リンゴ', 'ぶどう', 'バナナ', 'みかん'
    ]

    def __init__(self, money):
        self.money = money
        self.fruits = []

    def getMoney(self):
        return self.money

    def bet(self):
        dice = random.randint(1, 6)
        if dice == 1:
            self.money += 100
            print('所持金が増えました。')
        elif dice == 2:
            self.money /= 2
            print('所持金が半分になりました。')
        elif dice == 6:
            f = self.getFruit()
            print('フルーツ(' + f + ')をもらいました。')
            self.fruits.append(f)
        else:
            print('何も起こりませんでした。')

    def createMemento(self):
        m = Memento(self.money)
        for f in self.fruits:
            if f.startswith('おいしい'):
                m.addFruit(f)
        return m

    def restoreMemento(self, memento):
        self.money = memento.money
        self.fruits = memento.getFruits()

    def __str__(self):
        return '[money = ' + str(self.money) \
                     + ', fruits = ' + str(self.fruits) + ']'

    def getFruit(self):
        prefix = ''
        if random.randint(0, 1) == 1:
            prefix = 'おいしい'
        return prefix + \
            Gamer.fruitsname[random.randint(0, len(Gamer.fruitsname) - 1)]
