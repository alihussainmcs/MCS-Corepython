# OOPs concepts
"""
Class Object
Encapsulation
Abstraction
Inheritance
Polymorphism
"""
'''
# STATE    - data structures  - fields
# BEHAVIOR - functions        - methods

variables value                 #   x = 10
parameters arguments functions  #  def func(params)  func(args)
fields, methods                 #  Inside class 

'''

# Retrieve employee information  with hike 10% in an organization
# emp_data = [{'eid':100,'ename':'Madhu N','sal':10000},.......]
# Without oops concepts
# 1. Retrieve the emp data - RETRIEVAL/READ

print("-----Without oops concepts--------")
# STATE
emp_id = 101
emp_name = 'Ali Hussain'
e_sal = 10000


# BEHAVIOR


def get_edata(eid, name, sal):
    sal = sal + sal * 10 / 100
    print("Employee after Hike :", eid, " - ", name, " - ", sal)


get_edata(emp_id, emp_name, e_sal)

print("-----With oops concepts--------")


# class definition


class Employee:
    # STATE   # fields
    def __init__(self, eid, ename, sal):  # parameters
        self.eid = eid  # RHS --> Local variables
        self.ename = ename  # LHS --> Instance variables
        self.sal = sal  # self -> instance/object/ref variable

    # BEHAVIOR  # methods
    def get_emp_details(self):
        self.sal = self.sal + self.sal * 10 / 100
        print("Employee information :", self.eid, " - ", self.ename, " - ", self.sal)


# object creation
ali = Employee(1001, 'Ali H', 100000)  # Ali - object*/reference/instance  RHS - Object creation
ali.get_emp_details()

'''
        x = 10 
  varible = value     
parameter = argument    
object    = object creation
/instance/
ref. variable  

'''
kiran = Employee(1001, 'Kartik Kumar', 15000)
kiran.get_emp_details()

prakash = Employee(1002, 'Ayush Kumar', 20000)
prakash.get_emp_details()

# declaration     - int x
# initialization  - int x = 10

list1 = list([1, 2, 3])  # [1,2,3]
# list1 is an object of type list class(builtins.py)
# 0_sir_notes is an object of type Employee class


print("-----------Student class-----------------")


class Student:
    # STATE
    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks

    # BEHAVIOR
    def get_student_details(self):
        print("Student details : ", self.sid, self.name, self.marks)


s_id = 1010
sname = "Pythan"
smarks = 80

dilip = Student(s_id, sname, smarks)
dilip.get_student_details()

kartik = Student(31, 'Kartik Patel', 97)
kartik.get_student_details()

print(dilip, id(dilip), type(dilip))
# 10 int 10.5 float "hello" string

# class   n no of objects

print(dilip)
print(kartik)

print("...................................................................")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Ali", 24)

print(p1.name)
print(p1.age)

print("...........................................................................")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("Hello my name is " + self.name, 'and age ', self.age)


p1 = Person("John", 36)
p1.my_func()

print(".....................................................................")
# Instead of self we can use other string also but recommended self


class Person:
    def __init__(abc, name):
        abc.name = name

    def my_func(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Johny")
p1.my_func()
