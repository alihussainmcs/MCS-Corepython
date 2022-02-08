# Class for Dog
class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor

    def __init__(self, breed):
        # Instance Variable
        self.breed = breed

        # Adds an instance variable

    def setColor(self, color):
        self.color = color

    # Retrieves instance variable
    def getColor(self):
        return self.color

    # Driver Code


Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
print("..........................................................")


class BaseClass1:
    def __init__(self):
        print("Base class 1")


class BaseClass2:
    def __init__(self):
        print("Base class 2")


class DerivedClass(BaseClass1, BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self)
        BaseClass2.__init__(self)
        print("derived class")


ob = DerivedClass()
