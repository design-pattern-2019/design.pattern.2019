from ProgramNode import ProgramNode
from Context import Context

if __name__ == "__main__":
    try:
        with open("program.txt") as f:
            for text in f.readlines():
                text = "".join(text.splitlines())
                print("text = \"{}\"".format(text))
                node = ProgramNode()
                node.parse(Context(text))
                print("node = " + str(node))
    except Exception as e:
        import logging
        logging.exception(e)
