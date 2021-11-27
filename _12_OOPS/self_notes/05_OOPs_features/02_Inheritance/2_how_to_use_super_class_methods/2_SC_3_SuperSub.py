"""
SC 3: Few sub classes required
                     common behavior +
                     common** implementation   (Tiger,Lion)
      Remaining sub classes required
                     common behavior(method) +
                     unique** implementation  (Cat, Dog)


								Animal
									eating()
                Tiger   		Lion        Cat        Dog
					                          eating()   eating()

"""


class Animal:
    def __init__(self):
        pass
        # print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal Generic eating----")


class Tiger(Animal):
    def __init__(self):
        super().__init__()
        # print("SUB  :: Tiger constructor")


class Lion(Animal):
    def __init__(self):
        super().__init__()
        # print("SUB  :: Lion constructor")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        # print("SUB  :: Cat constructor")

    def eating(self):  # Method overriding
        print("SUB :: Cat eating----")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        # print("SUB  :: Dog constructor")

    def eating(self):  # Method overriding
        print("SUB :: Dog eating----")


anim = Animal()
anim.eating()

tiger = Tiger()
tiger.eating()

lion = Lion()
lion.eating()

cat = Cat()
cat.eating()

dog = Dog()
dog.eating()

print(".........................................................")


class EarthHuman:

    def __init__(self):
        print('Earth Human')

    def talk(self):
        print("Human talk language ........")


class IndiaHuman(EarthHuman):
    def __init__(self):
        super().__init__()
        print("India Human")

    def talk(self):
        print("India Human talk Hindi ........")


class ChinaHuman(EarthHuman):
    def __init__(self):
        super().__init__()
        print("China Human ")

    def talk(self):
        print("China Human talk Chinese ........")


class AmericaHuman(EarthHuman):
    def __init__(self):
        super().__init__()
        print("American Human ")

    def talk(self):
        print("America Human talk English........")


class UsaHuman(EarthHuman):
    def __init__(self):
        super().__init__()
        print("USA Human ")

    def talk(self):
        print("Usa Human talk English........")


eh = EarthHuman()
eh.talk()

ih = IndiaHuman()
ih.talk()

ch = ChinaHuman()
ch.talk()

ah = AmericaHuman()
ah.talk()

uh = UsaHuman()
uh.talk()

print(".............................................")


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    pass


x = Robot("Alien")
y = PhysicianRobot("Ali")
print(x, type(x))
print(y, type(y))
y.say_hi()
