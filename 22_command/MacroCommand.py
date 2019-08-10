from Command import Command

class MacroCommand(Command):
    __commands = []
    def execute(self) -> None:
        for cmd in self.__commands:
            cmd.execute()

    def append(self, cmd: Command) -> None:
        if (cmd is not self):
            self.__commands.append(cmd)

    def undo(self) -> None:
        if (not self.commands):
            self.__commands.pop()

    def clear(self) -> None:
        self.__commands.clear()

