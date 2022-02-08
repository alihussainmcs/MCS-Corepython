"""
We should not write concrete method in super class
Each sub class requires talks() behavior impl. in unique way
"""
# Without Abstraction


class EarthHuman:

    def __init__(self):
        print('Earth Human')

    def talk(self):
        print("Human talk ........")


class IndiaHuman(EarthHuman):

    def talk(self):
        print("India Human talk ........")


class AmericaHuman(EarthHuman):

    def talk(self):
        print("America Human talk ........")


class ChinaHuman(EarthHuman):

    def talk(self):
        print("China Human talk ........")


eh = EarthHuman()
eh.talk()

ih = IndiaHuman()
ih.talk()


ah = AmericaHuman()
ah.talk()

ch = ChinaHuman()
ch.talk()
