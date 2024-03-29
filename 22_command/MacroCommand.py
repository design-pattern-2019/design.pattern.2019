from Command import Command

class MacroCommand(Command):
    def __init__(self):
        self.__commands = []

    def execute(self) -> None:
        for cmd in self.__commands:
            cmd.execute()

    def append(self, cmd: Command) -> None:
        if (cmd is not self):
            self.__commands.append(cmd)

    def undo(self) -> None:
        if (self.__commands):
            self.__commands.pop()

    def clear(self) -> None:
        self.__commands.clear()

