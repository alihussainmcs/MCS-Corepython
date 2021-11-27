from abc import ABC, abstractmethod


# With Abstraction


class EarthHuman(ABC):
    @abstractmethod
    def talk(self):
        pass


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

print(".......................................................")


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        # "Abstarct Method"
        pass


# Sub class/ child class of abstract class
class SBI(Bank):
    def interest(self):
        # "Implementation of abstract method"
        print("In sbi bank 5 % interest")


s = SBI()
s.bank_info()
s.interest()
