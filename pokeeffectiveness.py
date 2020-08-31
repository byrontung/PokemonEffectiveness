import pandas as pd
EOF = ""
effectiveDict = {}
# data = pd.read_csv(
#     "D:\Code\GitHub\Random\PokemonEffectiveness\effectiveness.csv")

# print(data)


def csv_to_dict():
    effectiveDict = {}
    fname = open(
        "D:\Code\GitHub\PokemonEffectiveness\effectiveness.csv")
    # fname = open("effectiveness.csv", "r")
    labels = (fname.readline().strip()).split(",")
    line = fname.readline().strip()
    while line != EOF:
        templist = []
        tokens = line.split(",")
        index = [x for x in range(len(tokens)) if tokens[x] == "1"]
        index_to_words = [labels[i] for i in index]
        effectiveDict[tokens[0]] = set(index_to_words)
        line = fname.readline().strip()
    return effectiveDict


def user_input():
    print("_" * 80)
    fIn = input("What type is the pokemon? ")
    tokens = fIn.split(" ")
    while len(tokens) > 2 or len(tokens) == 0:
        fIn = input("Too many types, try again: ")
        tokens = fIn.split(" ")
    for i in range(len(tokens)):
        tokens[i] = tokens[i].title()
    return tokens


def fIn_to_1(token, effDict):
    # print(effectiveDict)
    info = {effDict[token[0]]}
    return list(info)


def fIn_to_2(tokens, effDict):
    type1 = effDict[tokens[0]]
    type2 = effDict[tokens[1]]
    botheff = type1 & type2
    return list(type1), list(type2), list(botheff)


# def getEffectiveness():
    # effectiveDict = csv_to_dict()
    # user_in = user_input()
    # while user_in != []:
    #     if len(user_in) == 1:
    #         eff = fIn_to_1(user_in, effectiveDict)
    #         print(f"\n{user_in[0]} is weak against {eff}\n")

    #     elif len(user_in) == 2:
    #         eff0, eff1, effo = fIn_to_2(user_in, effectiveDict)
    #         if effo == set():
    #             effo = None
    #         print(f"\n{user_in[0]} is weak against {eff0}")
    #         print(f"\n{user_in[1]} is weak against {eff1}")
    #         print(f"\nThis pokemon has a double weakness to {effo}\n")
    #         # print(eff1, eff2, effo, sep="\n", end="\n")
    #         # type1, type2, effo = fIn_to_2(user_in, effectiveDict)
    #     user_in = user_input()


def getEffectiveness():
    effectiveDict = csv_to_dict()
    user_in = user_input()
    while user_in != []:
        if len(user_in) == 1:
            eff = fIn_to_1(user_in, effectiveDict)
            return [eff, None, None]

        elif len(user_in) == 2:
            eff0, eff1, effo = fIn_to_2(user_in, effectiveDict)
            if effo == set():
                effo = None
            return [eff0, eff1, effo]
            # print(eff1, eff2, effo, sep="\n", end="\n")
            # type1, type2, effo = fIn_to_2(user_in, effectiveDict)
        user_in = user_input()


getEffectiveness()
