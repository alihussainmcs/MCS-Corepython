"""
                           Animal
                  Cat    Dog   Tiger    Lion

Own Specific method
Inherited method
Overridden method

"""


class Animal:
    def __init__(self):
        print("In Animal object")

    # Generic behavior
    def eating(self):
        print("Animal Eating")


class Cat(Animal):

    def __init__(self):
        print("In CAT object")

    # Specific behavior
    def sleeping(self):
        print("Cat is sleeping")

    # method overriding
    def eating(self):
        print("Cat is Eating")


cat = Cat()
cat.sleeping()
cat.eating()

# SCENARIOS
print("--------------------------")


class Dog(Animal):
    def __init__(self):
        print("In DOG object")

    # Specific behavior
    def barking(self):
        print("DOG is barking")


dog = Dog()
dog.barking()
dog.eating()

print("----------------------")


class Lion(Animal):
    def __init__(self):
        print("In LION object")


lion = Lion()
lion.eating()


print(".......................................................")
# Python program to demonstrate
# method overriding
# Defining parent class


class Parent:

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)


# Defining child class
class Child(Parent):

    # Constructor
    def __init__(self):
        super().__init__()
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)


obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()

print("...............................................................")


# Program to define the use of super()
# function in multiple inheritance
class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')

    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)


# class GFG2 inherits the GFG1
class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)


# class GFG3 inherits the GFG1 ang GFG2 both
class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()

    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)


gfg = GFG3()

# calling the function sub_GFG3() from class GHG3
# which inherits both GFG1 and GFG2 classes
gfg.sub_GFG(10)
