"""
python interpreted programming language

 .java   ---compilation ---> .class   --runtime->


Polymorphism : Ability to exists in multiple forms
2 types : Static polymorphism - compile time - Ex => Method Overloading
          Dynamic polymorphism - run time    - Ex => Method Overriding
"""

# Static polymorphism

'''
Method overloading in other languages:
---------------------------------------
class Employee:
    def getdata(eid):
        pass
    def getdata(eid,name):
        pass
    def getdata(eid,name,sal):
        pass

ali = Employee()
ali.getdata(10)  17th line
ali.getdata(10,'ali')  19th line
ali.getdata(10,'ali',1000) 21st line

in Python:
----------
def getdata(eid = 0, name = None, sal = 0):  # Method Overloading
    pass

getdata(10)
getdata(10,'ali')
getdata(10,'ali',1000)   
getdata(name='ali', sal=1000) 
getdata(name='ali')
getdata(sal=1000) 

'''

x = 10
print(x)
x = 20
print(x)


def getdata(eid):
    print("Data is : ", eid)


getdata(10)


def getdata(eid, name):
    print("Data is : ", eid, name)


# getdata(10)  # ERROR
getdata(10, 'ali')  # WORKS


def getdata(eid, name, sal):
    print("Data is : ", eid, name, sal)


# getdata(10)  # ERROR
# getdata(10, 'ali')  # ERROR
getdata(10, 'ali', 1000)


# Solution is use one single method with default arguments for parameters


def getdata(id=None, name=None, sal=None):  # Ex for static poly...
    print("Data : ", id, name, sal)


getdata()  # getdata(id=None,name=None,sal=None)
getdata(10)  # getdata(id=10,name=None,sal=None)
getdata(10, 'ali')  # getdata(id=10,name='ali',sal=None)
getdata(10, 'ali', 1000)  # getdata(id=10,name='ali',sal=1000)

'''
This method will exhibit Static polymorphism'''

# *args  **kwargs : Will see in decorator concept

print('Program to overload + operator for Book class objects:')


class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(100)
b2 = Book(200)
print('The Total Number of Pages:', b1 + b2)

"""
Overloading > and <= operators for Student class objects
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __le__(self, other):
        return self.marks <= other.marks


print("10>20 =", 10 > 20)
s1 = Student("Ali", 100)
s2 = Student("Hussain", 200)
print("s1>s2=", s1 > s2)
print("s1<s2=", s1 < s2)
print("s1<=s2=", s1 <= s2)
print("s1>=s2=", s1 >= s2)


class ClassA:
    def method1(self):
        print('this method belongs to class classA')


class ClassB:
    def method1(self, a):
        print('this method belongs to class classB')


ObjB = ClassB()
ObjB.method1(10)
'''
ObjB.method1()  

    ObjB.method1()  # it will return error so overloading will not support
TypeError: method1() missing 1 required positional argument: 'a'
'''
print('.......................................................')
print("Constructor overloading")


class Test:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        print('Constructor with 0|1|2|3 number of arguments')


t1 = Test()
t2 = Test(10)
t3 = Test(10, 20)
t4 = Test(10, 20, 30)

print('...........................................................')


class Test:
    @staticmethod
    def sum_1(a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('The Sum of 3 Numbers:', a + b + c)
        elif a is not None and b is not None:
            print('The Sum of 2 Numbers:', a + b)
        else:
            print('Please provide 2 or 3 arguments')


t = Test()
t.sum_1(10, 20)
t.sum_1(10, 20, 30)
t.sum_1(10)
