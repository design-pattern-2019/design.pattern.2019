from Node import Node
from CommandListNode import CommandListNode
from Context import Context
from ParseException import ParseException

class RepeatCommandNode(Node):
    def __init__(self):
        self.__number = None
        self.__commandListNode = None

    def parse(self, context: Context) -> None:
        context.skipToken("repeat")
        self.__number = context.currentToken()
        context.nextToken()
        self.__commandListNode = CommandListNode()
        self.__commandListNode.parse(context)

    def __str__(self):
        return "[repeat " + self.__number + " " + str(self.__commandListNode) + "]"
