# Dynamic polymorphism   ==> Method overriding
# From child class constructor we can call parent class constructor by using super() method.

class Animal:

    def __init__(self):
        pass

    def sleeping(self):
        print("Animal sleeping")


class Tiger(Animal):

    def __init__(self):
        super().__init__()

    def sleeping(self):  # Method overriding
        print("Tiger sleeping")


tiger = Tiger()
tiger.sleeping()

print('..........................................')


class P:
    def property(self):
        print('Gold+Land+Cash+Power')

    def marry(self):
        print('Appalachia')


class C(P):
    def marry(self):
        print('Katrina')


c = C()
c.property()
c.marry()

print("....................Constructor overriding..............")


class P:
    def __init__(self):
        print('Parent Constructor')


class C(P):
    def __init__(self):
        super().__init__()
        print('Child Constructor')


c = C()

print("...................................................................")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def display(self):
        print('Employee Name:', self.name)
        print('Employee Age:', self.age)
        print('Employee Number:', self.eno)
        print('Employee Salary:', self.esal)


e1 = Employee('Ali', 24, 872425, 26000)
e1.display()
e2 = Employee('Ila', 42, 872426, 36000)
e2.display()

print("...................................................................")


class A(object):  # inherit from base object
    def show(self):  # define function to inherit
        print("Base class")


class B(A):  # inherit from A
    def show(self):  # override A.show()
        print("Derived class")


a = B()  # instance of derived class B
a.show()  # would print "Derived class"
