"""
OVERRIDE *
II: All sub classes required  : a. Common  signature and
                                b. unique implementation

                            --> method signature -  common behavior
                            --> method body      -  unique** implementation


   If we write classes without inheritance as below,
                 Tiger   		Lion        Cat        Dog
					 eating()    eating()    eating()   eating()
	We cant understand common behavior.
	So this will not work out.

    ==> We have to use inheritance mechanism here

								Animal
									eating()

                Tiger   		Lion        Cat        Dog
					 eating()    eating()    eating()   eating()

Above mechanism is called as Method Overriding **

"""


class Animal:

    def __init__(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Generic Behavior")  # Generic impl.


class Tiger(Animal):

    def __init__(self):
        print("SUB  :: Tiger constructor")

    def eating(self):  # Method overriding
        print("SUB :: Tiger eating in specific manner ")  # specific (our own) impl.


tiger = Tiger()
tiger.eating()


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

print("................................................................")


class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi())
print("SBI Rate of interest:", b2.getroi())
print("ICICI Rate of interest:", b3.getroi())
