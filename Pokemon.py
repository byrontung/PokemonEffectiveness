import pandas as pd

from pokeeffectiveness.py import

df = pd.read_csv("Pokemon.csv")
# pokemon = df["Name"]
# mask = df["Name"] == "Charizard"
# info = df[mask]
# # row from csv
# print(info)
# # row from csv into seperate line
# print(info.iloc[0])
# # row from csv into seperate line where the label == "#"
# print(info.iloc[0]["#"])
# # a = (df["Name"] == "Charizard").any()
# # print(f"this is a: {a}")


class Pokemon:

    # assume that I get a correct name for a pokemon
    def __init__(self, name):
        self.name = name.title()
        self.type1 = None
        self.type2 = None
        self.legendary = None
        # self.effective = []

# this is to make sure the name is valid, name should be titleized
    def getInfo(self):
        mask = df["Name"] == name
        info = df[mask]
        self.type1 = info.iloc[0]["Type 1"]
        self.type2 = info.iloc[0]["Type 2"]
        self.legendary = info.iloc[0]["Legendary"]
