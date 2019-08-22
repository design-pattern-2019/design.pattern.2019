from Tokenizer import Tokenizer
from ParseException import ParseException

class Context():
    def __init__(self, text: str):
        self.__tokenizer = Tokenizer(text)
        self.__currentToken = None
        self.nextToken()

    def nextToken(self) -> str:
        if self.__tokenizer.hasMoreTokens():
            self.__currentToken = self.__tokenizer.nextToken()
        else:
            self.__currentToken = None
        return self.__currentToken

    def currentToken(self) -> str:
        return self.__currentToken

    def skipToken(self, token: str) -> None:
        if not token == self.__currentToken:
            raise ParseException("Warning {} is expected, but {} is found".format(token, self.__currentToken))
        self.nextToken()

    def currentNumber(self) -> int:
        number: int = 0
        try:
            number = int(self.__currentToken)
        except ValueError as e:
            raise ParseException("Warning: " + str(e))
        return number
