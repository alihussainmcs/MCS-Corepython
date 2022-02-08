"""
Inheritance Types:
-------------------
Simple / Single  : Super 1 , Sub 1
Multi level      : Super 1, Sub 1,  SubSub 1
Hierarchical      : Super 1,  Sub 2 or more
Hybrid           : Comb of multi level + Hierarchical
Multiple**       : One sub class with 2 or more super classes
"""
# Simple / Single  : Super 1 Sub 1
'''
A
|
B
'''
print("-----------1. Simple Inheritance----------")


class A:
    def m1(self):
        print("A m1()")


class B(A):
    def m2(self):
        print("B m2()")


'''
B class has 2 methods - m1() inherited method
                      - m2() its own method

'''
print("-----------2. Multi level Inheritance----------")

# Multi level Inheritance      : Super 1 Sub 1  SubSub 1
'''
A     Polygon
|
B       Quadrilateral
|
C            Square
'''


class A:
    def m1(self):
        print("A m1()")


class B(A):
    def m2(self):
        print("B m2()")


class C(B):
    def m3(self):
        print("C m3()")


'''
C has 3 behaviors - m1() inherited method from A
                  - m2() inherited method from B
                  - m3() its own method
'''
a = A()
a.m1()
# a.m2()  # ERROR

b = B()
b.m1()
b.m2()
# b.m3() # ERROR

c = C()
c.m1()
c.m2()
c.m3()
# c.m4()  # ERROR

print("-----------3. Hierarchial Inheritance----------")

# Hierarchial      : Super 1 Sub 2 or more
'''
   A
/  |  \
B  C   D   

'''


class A:
    def m1(self):
        print("A m1()")


class B(A):
    def m2(self):
        print("B m2()")


class C(A):
    def m3(self):
        print("C m3()")


class D(A):
    def m4(self):
        print("D m4()")


print("-----------4. Hybrid Inheritance----------")

# Hybrid           : Comb of multi level + Hierarchical
'''
     A 
     |
     B
    / \
   C   D    
  /     \ 
  E     F
'''

print("-----------5. Multiple Inheritance----------")

# Multiple  **       : One sub class with 2 or more super classes
'''
  A     B
   \   / 
     C
'''


class A:
    def m1(self):
        print("A m1()")


class B:
    def m2(self):
        print("B m2()")


class C(A, B):  # Order of precendence is first A,then B
    def m3(self):
        print("C m3()")


'''
C has 3 behaviors   - m1()  inherited from A
                    - m2()  inherited from B
                    - m3()  specific or own method
'''

c = C()
c.m1()
c.m2()
c.m3()

print("--------Problem with multiple inheritance---------")


class A:
    def m1(self):
        print("A m1()")


class B:
    def m1(self):
        print("B m1()")


# method resolution order principle
class C(A, B):  # MRO principle Left --> Right
    def m3(self):
        print("C m3()")


c = C()
c.m3()
c.m1()


class A:
    a = 100

    def __init__(self):
        print("in A init method")

    def m1(self):
        print("A - m1() method")

    def download_file(self):
        print("A - download_file() method ==> pdf ")


class B(A):
    def __init__(self):
        A.__init__(self)  # first initialize super class state **
        print("in B init method")

    def m3(self):
        print("B - m3() method")

    def download_file(self):  # Method overriding
        print("B - download_file() method ==> excel ")


b = B()
b.m1()
b.download_file()
b.m3()
# b.m4()

'''
a = A()
a.m1()
a.m2()
#a.m3()
'''
print("-------Simple inheritance--------------")


class A:
    def m1(self):
        print("A m1()")

    def a(self):
        print("A a()")


class B(A):
    def m1(self):  # Method overriding
        print("B m1()")

    def m2(self):
        print("B m2()")


b = B()
b.m1()
b.m2()
b.a()

print("--------Multi level inheritance-----------------")


class A:
    def m1(self):
        print("A m1()")

    def a(self):
        print("A a()")


class B(A):
    def m1(self):
        print("B m1()")

    def m2(self):
        print("B m2()")


class C(B):
    def m3(self):
        print("C m3()")


c = C()
c.m1()
c.m2()
c.a()
c.m3()
print(c)  # c.__str__()

print("--------Multiple inheritance-----------------")


class A:
    def m1(self):
        print("A m1()")


class B:
    def m1(self):
        print("B m1()")


class C(B, A):  # MRO - Method Resolution Order*
    pass


c = C()
c.m1()

'''
diamond problem
   A 
 B    C
   D 
'''

print("......................................................")


# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    # creation of an object variable or an instance


a = Employee('Ali', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()
