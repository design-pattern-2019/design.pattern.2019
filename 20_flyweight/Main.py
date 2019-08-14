import sys

from BigString import BigString


class Main:
    args = sys.argv
    if len(args) == 1:
        print('Usage: python Main.py digits')
        print('Example: python Main.py 1212123')
        sys.exit()

    bs = BigString(args[1])
    bs.print()


if __name__ == "__main__":
    Main
