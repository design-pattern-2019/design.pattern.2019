class Tokenizer():
    def __init__(self, text: str):
        self.__tokens = text.split(" ")
        self.__index = 0

    def nextToken(self):
        nextToken = self.__tokens[self.__index]
        self.__index += 1
        return nextToken

    def hasMoreTokens(self):
        return self.__index < len(self.__tokens)
