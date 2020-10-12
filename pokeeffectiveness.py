import pandas as pd
EOF = ""
effectiveDict = {}

df = pd.read_csv("./pokemon.csv", engine ='python')


def csv_to_dict():
    effectiveDict = {}
    fname = open("effectiveness.csv", "r")
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
    fIn = input("What is the pokemon? ").title()
    mask = df["Name"] == fIn
    info = df[mask]
    while info.empty and fIn != "Exit":
        print("_" * 80)
        fIn = input("Pokemon not found, try again: ").title()
        mask = df["Name"] == fIn
        info = df[mask]
    return fIn


def fIn_to_1(token, effDict):
    # print(effectiveDict)
    info = {effDict[token[0]]}
    return list(info)


def fIn_to_2(tokens, effDict):
    type1 = effDict[tokens[0]]
    try:
        type2 = effDict[tokens[1]]
    except:
        type2 = set()
    botheff = type1 & type2
    return type1, type2, botheff


def getEffectiveness(type1, type2):
    effectiveDict = csv_to_dict()
    if type2 != "nan":
        types = [type1, type2]
    else:
        types = [type1, None]
    eff0, eff1, effo = fIn_to_2(types, effectiveDict)
    if effo == set():
        effo = None
    return [eff0, eff1, effo]
