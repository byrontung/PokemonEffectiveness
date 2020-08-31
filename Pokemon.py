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
        printstr = f"{self.name}: {type1}, {type2}

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
        print(f"""
        {self.type1} is weak against {self.effective[0]}
        {self.type2} is weak against {self.effective[1]}
        {self.name} has a double weakness against {self.effective[2]}
                """)
