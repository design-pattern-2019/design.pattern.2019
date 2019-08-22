from Node import Node
from Context import Context
from ParseException import ParseException

class PrimitiveCommandNode(Node):
    def __init__(self):
        self.__name = None

    def parse(self, context: Context) -> None:
        self.__name = context.currentToken()
        context.skipToken(self.__name)
        if (self.__name != "go"
            and self.__name != "right"
            and self.__name != "left"):
            raise ParseException(self.__name + " is undefined")

    def __str__(self):
        return self.__name
