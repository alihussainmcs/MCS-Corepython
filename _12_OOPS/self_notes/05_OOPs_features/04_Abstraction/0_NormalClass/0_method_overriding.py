class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    def say_hi(self):                           # method overriding
        print("Everything will be okay! ")
        print(self.name + " takes care of you!")


y = PhysicianRobot("Ali")
y.say_hi()


print(".........................................................")


class EarthHuman:

    def __init__(self):
        print('Earth Human')

    def talk(self):
        print("Human talk ........")


class IndiaHuman(EarthHuman):
    def __init__(self):
        super().__init__()
        print("India Human")

    def talk(self):
        print("India Human talk ........")


class AmericaHuman(EarthHuman):
    def __init__(self):
        super().__init__()
        print("American Human ")

    def talk(self):
        print("America Human talk ........")


class ChinaHuman(EarthHuman):
    def __init__(self):
        super().__init__()
        print("China Human ")

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
