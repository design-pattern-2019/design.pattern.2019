from abc import ABCMeta, abstractmethod


class Support(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    def setNext(self, next):
        self.next = next
        return self.next

    def support(self, trouble):
        if self.resolve(trouble):
            self.done(trouble)
        elif hasattr(self, 'next'):
            self.next.support(trouble)
        else:
            self.fail(trouble)

    def __str__(self):
        return '[' + self.name + ']'

    @abstractmethod
    def resolve(self, trouble):
        pass

    def done(self, trouble):
        print(str(trouble) + ' is resolved by ' + str(self) + '.')

    def fail(self, trouble):
        print(str(trouble) + ' cannot be resolved.')
