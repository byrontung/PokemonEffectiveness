from Pokemon import *
from menu import menu


def main():
    # user_in = user_input()
    # while user_in != "Exit":
    #     pokemon = Pokemon(user_in)
    #     pokemon.getInfo()
    #     pokemon.printeffective()
    #     user_in = user_input()
    repeat = menu()
    while repeat == True:
        repeat = menu()


if __name__ == "__main__":
    main()
