from Node import Node
from Context import Context
from CommandListNode import CommandListNode

class ProgramNode(Node):
    def __init__(self):
        self.__commandListNode: Node = None

    def parse(self, context: Context) -> None:
        context.skipToken("program")
        self.__commandListNode = CommandListNode()
        self.__commandListNode.parse(context)

    def __str__(self):
        return "[program " + str(self.__commandListNode) + "]"
