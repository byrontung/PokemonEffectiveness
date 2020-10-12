from Pokemon import *


def menu():
    options = ["1", "2", "exit"]
    user_types = ['nan', 'nan']
    print("_" * 80)
    menu_input = input(
        "1 - Type Effectiveness|\n2 - Pokemon Effectiveness: ").lower()
    while menu_input not in options:
        menu_input = input("Menu - Try again: ").lower()
        print(menu_input)
    if menu_input == 'exit':
        return 0
    elif menu_input == "1":
        type_input = input("Enter your type(s): ").title().split()
        while len(type_input) <= 0 or len(type_input) > 2:
            type_input = input("Types - Try again: ").title().split()
        for i in range(len(type_input)):
            user_types[i] = type_input[i]
        type_eff = getEffectiveness(user_types[0], user_types[1])
        print(type_eff)  # change the formatting for the print.

    elif menu_input == "2":
        user_in = user_input()
        pokemon = Pokemon(user_in)
        pokemon.getInfo()
        pokemon.printeffective()

        # while user_in != "Exit":
        #     pokemon = Pokemon(user_in)
        #     pokemon.getInfo()
        #     pokemon.printeffective()
        #     user_in = user_input()
    return 1
