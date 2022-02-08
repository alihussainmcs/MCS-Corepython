"""
SC1: As a sub class, I. inherit all super class methods
                     II.create your own methods

SC2: As a sub class, I. inherit all super class methods,override if required
                     II.create your own methods
"""


# SC 1
class A:
    def __init__(self):
        print("SUPER : A constructor ")

    def read(self):
        print("A reading")


# A has one behavior read()
class B(A):

    def __init__(self):
        print("SUB : B constr")

    def write(self):
        print("B writing")


# B has two behaviors read() write()
a1 = A()
a1.read()

b1 = B()
b1.read()  # inherited method
b1.write()  # sub class specific method


# SC2
class A:
    def __init__(self):
        print("SUPER : A constr")

    def read(self):
        print("A reading")

    def execute(self):
        print("A executing")


# A has 2 behaviors read() execute()

class B(A):

    def __init__(self):
        print("SUB : B constr")

    def read(self):  # method overriding
        print("B reading")

    def write(self):
        print("B writing")


'''
B has 3 behaviors   - execute() from super class through inheritance
                    - read() i.e, from sub class overridden method
                    - write() from sub class(its  own method)

a1 = A()
a1.read()

b1 = B()
b1.read()
b1.write()

Inherited method  : execute()
Overridden method  : read()
Own method        : write()

'''

print(".........................................................")


class EarthHuman:

    def __init__(self):
        print('Earth Human')

    def talk(self):
        print("Human talk ........")


class IndiaHuman(EarthHuman):
    def __init__(self):
        print("India Human")

    def talk(self):
        print("India Human talk ........")


class AmericaHuman(EarthHuman):
    def __init__(self):
        print("American Human ")

    def talk(self):
        print("America Human talk ........")


class ChinaHuman(EarthHuman):
    def __init__(self):
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

print("......................................................")


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, I am " + self.name)


class PhysicianRobot(Robot):
    def say_hi(self):
        print("Everything will be okay! ")
        print(self.name + " takes care of you!")


y = PhysicianRobot("Ali")
y.say_hi()
