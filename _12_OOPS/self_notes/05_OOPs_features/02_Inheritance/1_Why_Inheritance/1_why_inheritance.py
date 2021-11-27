"""
Parent
Children
"""

'''
is-a relationship    <SUB> is a <SUPER>

2 classes: 
    Super   - Sub* 
    Parent  - Child* 
    Base    - Derived 

                   Animal
             |                 |
         Wild                   Domestic
         |  |                    |     |
    Tiger   Lion              Cat       Dog 

Without inheritance:
---------------------
Tiger, Lion, Cat, Dog 

    Tiger        Lion              Cat         Dog 
      eating()    eating()           eating()   eating()   # Code duplication

With inheritance:
---------------------
                   Animal
        Tiger   Lion         Cat    Dog 

                       Animal
                         eating()            # code re-usability, avoids code duplication
             |        |           |       |  
         Tiger        Lion        Cat     Dog 

Inheritance => is-a relationship **
Aggregation => has-a relationship  # Controller-Service-DAO layer

Tiger is a Animal     - TRUE
Lion is a Animal      - TRUE
Cat is a Animal       - TRUE
Dog is a Animal       - TRUE
SEmployee is a Animal - FALSE 

   FileWriter
pdf excel ppt word

LED TV is a TV
LCD TV is a TV
Laptop is a TV

SOLID Principles :  Single responsibility Principle
'''


class Animal:

    def __init__(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")


class Tiger(Animal):

    def __init__(self):
        print("SUB  :: Tiger constructor")

    def sleeping(self):
        print("SUB  :: Tiger sleeping")


print("--------super class object creation--------")
animal = Animal()
animal.eating()

print("--------sub class object creation--------")
tiger = Tiger()  # Tiger tiger = new Tiger()  int x = 10
tiger.eating()  # inherited super class method
tiger.sleeping()  # sub class specific method


class Dog(Animal):

    def __init__(self):
        print("SUB :: Dog constructor")

    def bark(self):
        print("SUB :: Dog Barking")


print("--------DOG : sub class object creation--------")
dog = Dog()
dog.eating()
dog.bark()


# Aggregation has-a relationship

# Employee has a Address


class Address:
    def __init__(self, hno, flatno, area, line, city, pincode, state):
        pass


class Employee:
    def __init__(self, id_1, name, sal, address):
        self.id_1 = id_1
        self.name = name
        self.sal = sal
        self.address = address


addr = Address(123, 205, 'Wilson Garden', '2nd line', 'Bangalore', 560037, 'Karnataka')
madhu = Employee(101, 'Ali H', 10000, addr)

# Employee has a address
print("......................................................")


class University:
    def __init__(self):
        print("Super Pass")

    @staticmethod
    def branch(b_name):
        print("Branch :", b_name)


class College(University):
    def __init__(self):
        print('Sub Pass')


u1 = College()
u1.branch('CSE')

print("............................................")


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
print(d.Summation(10, 20))
print(d.Multiplication(10, 20))
print(d.Divide(10, 20))
