from Node import Node
from Context import Context
from ParseException import ParseException

class CommandListNode(Node):
    def __init__(self):
        self.__list = []

    def parse(self, context: Context) -> None:
        from CommandNode import CommandNode
        while True:
            if context.currentToken() == None:
                raise ParseException("Missing 'end'")
            elif context.currentToken() == "end":
                context.skipToken("end")
                break
            else:
                commandNode = CommandNode()
                commandNode.parse(context)
                self.__list.append(commandNode)

    def __str__(self):
        return "[{}]".format(" ".join(list(map(str, self.__list))))
