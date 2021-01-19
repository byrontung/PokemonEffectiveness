from Pokemon import *
from menu import menu
from pokeeffectiveness import *


#add pathlib for path organization https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
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
