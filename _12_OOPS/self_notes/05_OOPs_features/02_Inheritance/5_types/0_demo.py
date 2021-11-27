# Code re-usability
"""
Grand Father      - Father
Father  - Parent  - Child
Son     - Child

Parent class
Child class

Super class
Sub class

Base class
Derived class
"""
"""
                              Animal

                DomesticAnimal        WildAnimal
                  Cat    Dog             Tiger Lion


                           Animal
                  Cat    Dog   Tiger    Lion

"""

'''
XX ==> Only Super class : Animal,Employee : Unnecessarily other behavior also will come to our object

XX ==> Only Sub classes : Code duplication. For example one method is common for all classes,then code duplication will happen

Solution : Use Inheritance 
           Implement classes as Super class - Sub class mechanism
'''


class Animal:
    def __init__(self):  # Common state
        print("In Animal object")

    # Generic behavior

    def eating(self):  # Common behavior for all sub classes
        print("Animal Eating")


class Cat(Animal):  # Cat is-a Animal

    def __init__(self):
        print("In CAT object")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

    def eating(self):  # Method overriding
        print("Cat Eating")


animal = Animal()
animal.eating()

# animal.sleeping()
print("-----------------")

cat = Cat()
cat.sleeping()
cat.eating()
'''
Here Cat is sub class and Animal is super class. 
Cat as a sub class wil inherit all the features of Animal
Inheritance should be applicable when IS-A *** relationship is satisfied

'''


# Method overriding ==> Dynamic polymorphism
print(".............................................")


class A:
    def __init__(self, n='Ali'):
        self.name = n


class B(A):
    def __init__(self, roll):
        super().__init__()
        self.roll = roll


obj = B(23)
print(obj.name)
