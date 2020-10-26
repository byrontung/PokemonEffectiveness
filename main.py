from Pokemon import *
from menu import menu
from pokeeffectiveness import *


def main():
    repeat = menu()
    while repeat == True:
        repeat = menu()


if __name__ == "__main__":
    main()
