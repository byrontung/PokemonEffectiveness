from Pokemon import *


def main():
    user_in = user_input()
    while user_in != "Exit":
        pokemon = Pokemon(user_in)
        pokemon.getInfo()
        pokemon.printeffective()
        user_in = user_input()


if __name__ == "__main__":
    main()
