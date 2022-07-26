from Pokemon import *
from menu import menu
from pokeeffectiveness import *


#add pathlib for path organization https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
def main():
    repeat = menu()
    while repeat == True:
        repeat = menu()


if __name__ == "__main__":
    main()
