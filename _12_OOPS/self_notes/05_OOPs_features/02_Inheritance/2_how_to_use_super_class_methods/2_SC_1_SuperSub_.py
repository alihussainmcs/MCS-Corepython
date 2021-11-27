"""
def eating(self):
    print("SUPER :: Animal : eating")
    ....
Method:
        I.  Method signature   ==> def eating(self):
        II. Method body(impl.) ==> print("SUPER :: Animal : eating") ...

Code re-usability :  1. Signature + Body (Implementation)
                    2. Only signature

"""

'''  REUSE*
I: All sub classes required 
                method signature -  common  
                method body      -  common** implementation

                        Animal
                          - eating()
                Tiger   Lion     Cat   Dog
'''


class Animal:

    def __init__(self):
        pass
        # print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")


class Tiger(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Tiger constructor")


class Lion(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Lion constructor")


class Cat(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Cat constructor")


class Dog(Animal):

    def __init__(self):
        pass
        # print("SUB  :: Dog constructor")


ani = Animal()
ani.eating()

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

print("................................................")


class Calculation1:
    def Summation(self, a, b):
        return a + b


class Calculation2:
    def Multiplication(self, a, b):
        return a * b


class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b


d = Derived()
print(issubclass(Derived, Calculation2))
print(issubclass(Calculation1, Calculation2))
