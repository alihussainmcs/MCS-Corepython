"""
Object Oriented Programming System
"""

'''
Class/Object

Encapsulation
Abstraction
Inheritance
Polymorphism
'''

# REQUIREMENT : Sum of 2 given numbers

# STATE :   -  Data Initialization  ==> Data types/data structures
n1 = 10  # int(input("Enter number1"))
n2 = 20  # int(input("Enter number2"))


# BEHAVIOR   - Implementation       ==>  Functions


def get_sum(num1, num2):
    result = num1 + num2
    return result


print("Sum of 2 numbers is : ", get_sum(n1, n2))

'''
   if elif else 
   for while 
   functions 
   class 
   try except finally 
   with
'''

# class structure
'''
class <class-name>:
        # 1. STATE
    n1 = 10
    n2 = 20

        # 2. BEHAVIOR
    def get_sum(num1, num2):
        result = num1 + num2
        return result
'''

# REQ : Display each employee information   CRUD -> RETRIEVAL
'''
CRUD 
Data type/structures
STATE
BEHAVIOR
'''
# A1 :: Using Functions
# 1. STATE
print("..................Using Function .......................")
empid = 101
name = 'Ali'
sal = 25000


# 2. BEHAVIOR


def get_einfo(eid, ename, esal):
    print("Employee details are ", eid, ename, esal)


get_einfo(empid, name, sal)


# Using OOPs  -- Class

# Step 1:
# Not the proper way to write class


class Employee_1:
    # 1. STATE
    empid = 101  # int(input("Enter empid :"))
    name = 'Ali Hussain'  # input("Enter name : ")
    sal = 15000  # int(input("Enter sal :"))

    # 2. BEHAVIOR
    def get_einfo(eid, ename, esal):
        print("Employee details are ", eid, ename, esal)


# Step 2:
print("..............Using class .........................")


class Employee:

    # 1. STATE
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal

    # 2. BEHAVIOR
    def get_einfo(self):
        print("Employee details are ", self.empid, self.name, self.sal)


# object creation
ali = Employee(101, 'Al Hussain', 15000)  # x = 10
ali.get_einfo()

print(".....................2nd example of class ...................")


class Student:

    # 1. STATE
    def __init__(self, r_no, name, marks):
        self.r_no = r_no
        self.name = name
        self.marks = marks

    # 2. BEHAVIOR
    def get_sinfo(self):
        print("Student details are ", self.r_no, self.name, self.marks)


ali = Student(16, 'Jokar', 65)
ali.get_sinfo()
print(".....................3rd example of class ...................")


class Univercity:
    # State
    def __init__(self, u_name, u_id, u_add):
        self.u_name = u_name
        self.u_id = u_id
        self.u_add = u_add

    # Behaviour
    def uni(self):
        print("Univercity Details : ", self.u_name, self.u_id, self.u_add)


clg1 = Univercity("RGPV", 4620, "MP")
clg1.uni()
print(".....................4th example of class ...................")


class Mask:
    def __init__(self, m_name, m_price, m_clr):
        self.m_name = m_name
        self.m_price = m_price
        self.m_clr = m_clr

    def mas(self):
        print("Mask details :", self.m_name, self.m_price, self.m_clr)


mask1 = Mask("N-95", 75, "Green")
mask1.mas()

print("..........................................................................")


class Car(object):
    def __init__(self, name, price, fuel, speed, mileage, tax):
        self.name = name
        self.price = price
        self.speed = speed
        self.mileage = mileage
        self.fuel = fuel
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print("=====" + self.name + "=====")
        print("Price: $" + str(self.price))
        print("Speed: " + str(self.speed) + "mph")
        if self.fuel == 1.0:
            print("Fuel: Full")
        else:
            print("Fuel: " + str(self.fuel * 100) + "%")
        print("Mileage: " + str(self.mileage) + "mph")
        print("Tax: " + str(self.tax * 100) + "%")


honda = Car("Honda", 10000, 1.0, 60, 10, 0.10)
honda.display_all()

toyota = Car("Toyota", 30000, 1.0, 70, 15, 0.10)
toyota.display_all()

ford = Car("Ford", 40000, 0.5, 80, 20, 0.10)
ford.display_all()

corvette = Car("Corvette", 50000, 0.25, 90, 25, 0.10)
corvette.display_all()

bmw = Car("BMW", 60000, 0.75, 100, 35, 0.10)
bmw.display_all()

hyundai = Car("Hyundai", 70000, 1.25, 1000, 1000, 0.10)
hyundai.display_all()
