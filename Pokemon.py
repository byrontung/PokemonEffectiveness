import pandas as pd

from pokeeffectiveness import *


class Pokemon:

    # assume that I get a correct name for a pokemon
    def __init__(self, name):
        self.name = name.title()
        self.type1 = None
        self.type2 = None
        self.legendary = None
        self.effective = None

    def __str__():
        if self.type2 == None:
            return f"{self.name} - types:{type1} - weakness:{self.effective}"
        else:
            return f"{self.name} - types:{type1}{type2} - weakness:{self.effective}"

    def getInfo(self):
        mask = df["Name"] == self.name
        info = df[mask]
        self.type1 = info.iloc[0]["Type 1"]
        if (pd.isnull(info.iloc[0]["Type 2"])):
            self.type2 = None
        else:
            self.type2 = info.iloc[0]["Type 2"]
        self.legendary = info.iloc[0]["Legendary"]
        self.effective = getEffectiveness(self.type1, self.type2)

    def getname(self):
        return self.name

    def gettypes(self):
        return [type1, type2]

    def getlegendary(self):
        return self.legendary

    def printeffective(self):
        print(f"\n\t{self.type1} is weak against {self.effective[0]}")
        if self.type2:
            print(f"\t{self.type2} is weak against {self.effective[1]}")
        if self.effective[2]:
            print(f"\t{self.name} has a double weakness against {self.effective[2]}")
        else:
            print(f"\t{self.name} does not have a double weakness")
        print()