# Dynamic polymorphism   ==> Method overriding

class Animal:

    def __init__(self):
        pass

    def sleeping(self):
        print("Animal sleeping")

class Tiger(Animal):

    def __init__(self):
        pass

    def sleeping(self): # Method overriding
        print("Tiger sleeping")


tiger = Tiger()
tiger.sleeping()