class EarthHuman:
    """
    def __init__(self):
        print('Human Pass')

    """

    def talk(self):
        print("Human talk ........")


class IndiaHuman(EarthHuman):
    def __init__(self):
        print("India Human Pass")


ih = IndiaHuman()
ih.talk()


class AmericaHuman(EarthHuman):
    def __init__(self):
        print("American Human ")


ah = AmericaHuman()
ah.talk()


class ChinaHuman(EarthHuman):
    def __init__(self):
        print("China Human ")


ch = ChinaHuman()
ch.talk()
