from Node import Node
from Context import Context
from RepeatCommandNode import RepeatCommandNode
from PrimitiveCommandNode import PrimitiveCommandNode

class CommandNode(Node):
    def __init__(self):
        self.__node = None
    def parse(self, context: Context):
        if context.currentToken() == "repeat":
            self.__node = RepeatCommandNode()
            self.__node.parse(context)
        else:
            self.__node = PrimitiveCommandNode()
            self.__node.parse(context)

    def __str__(self):
        return str(self.__node)
