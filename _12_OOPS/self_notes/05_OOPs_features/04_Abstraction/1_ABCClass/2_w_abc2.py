from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

    def details(self):
        print("Concrete methods")


class Human(Animal):
    pass


class Dog(Animal):
    def move(self):
        print("I am Dog and I can bark")


class Lion(Animal):
    def move(self):
        print("I can roar")


class Snake(Animal):
    def move(self):
        print("I can crawl")

    # c=Animal() # TypeError: Can't instantiate abstract class Animal with abstract methods move


# hu_obj = Human()  TypeError: Can't instantiate abstract class Human with abstract methods move
# hu_obj.move()

dog_obj = Dog()
dog_obj.move()

print(".............................................................")


# Abstract Class
class Bank(ABC):
    def bank_info(self):
        print("Welcome to bank")

    @abstractmethod
    def interest(self):
        # "Abstarct Method"
        pass

    def offers(self):
        print("Providing offers")
    # Sub class/ child class of abstract class


class SBI(Bank):
    def interest(self):
        print("In SBI bank 5 % interest")


class HDFC(Bank):
    def interest(self):
        print("In HDFC 7 % interest")


s = SBI()
h = HDFC()
s.bank_info()
s.interest()
h.bank_info()
h.interest()
