"""

http://www.python-course.eu/python3_inheritance.php
http://www.python-course.eu/inheritance_example.php
"""
'''
                    Polygon
                       p1()
     Triangle                   Quadrilateral                         Pentagon Hexagon 
        t1()                        q1()   
    ET      RA    IS         Square Rhombus Rectangle Parll 
    e1()    r1()  i1()       s1()   r1()    re1()      pa1()

Sub class ---is a -- super class
RA is a Polygon 
RA is a Triangle 
R  is a Polygon 
R  is a Quadrilateral
Re is a Polygon 
Re is a Quadrilateral
Re is a Pentagon

wrt Polygon
Polygon is super class
T Q P H are sub classes wrt Polygon 

wrt to Triangle 
Triangle is super class
E RA Is sub classes of Triangle
E RA Is sub classes of Polygon

    Employee:
        get_emp_details()
PermaE       ContrE 
 get_pf()       get_gratuity()



Student

Office 



Super/Parent/Base  class
Sub/Child/Derived  class

                    Pentagon
                       m1()         
        Triangle Quadrilateral Pentagon Hexagon 

'''


class Employee:

    def __init__(self, eid, name):
        self.eid = eid
        self.name = name

    def get_emp_details(self):
        print("In Super Class : get_emp_details()")

    def get_info(self):
        print("In Super class : get_info()")


class SoftwareEmployee(Employee):  # IS - A

    def __init__(self, eid, name, sal):
        Employee.__init__(self, eid, name)  # super().__init__(self, fName, lName)
        self.sal = sal

    def get_sw_emp_details(self):
        print("-------In Sub Class : get_sw_emp_detailsI()-------------")


ali = Employee(100, 'Ali H')
ali.get_emp_details()
ali.get_info()
ali1 = SoftwareEmployee(101, 'H Ali', 20000)

ali = SoftwareEmployee(11, "Ali Hussain", 1000)
print("*******************************")
ali.get_sw_emp_details()
ali.get_emp_details()
ali.get_info()

pavan = Employee(110, "Pavan Kumar Ball")

pavan.get_emp_details()

print("Object   content is ", pavan)
print("Object   content is ", pavan.__str__())
print("Damu object ", pavan.__str__())
gopi = Employee(111, "Gopi")

# print("Adding 2 objects of employee ", pavan + gopi)    #damu.__add__(gopi)


ali.get_emp_details()
print("*******************************")
print("Type ", type(ali))

dict1 = {1: 1, 2: 2}
print("fdasfs", dict1.values())

'''
Inheritance Types :
------------------------
1. Simple Inheritance      Super class <---- Sub class
2. Multilevel Inheritance  Super class <---- Sub class  <---- Sub class
3. Hierarchical Inheritance               Super class 
                                    SubClass    SubClass SubClass  

4. Mulitple Inheritance **     SuperClass   SuperClass
                                        SubClass

5. Hybrid Inheritance 
                                        S      S 
                                            S
                                        S      S 
'''
'''      
#MRO - Method Resolution order
# Multiple Inheritance  
         A        B
         m1()     m2()   
              C
             m3()


'''
print("----------Multiple Inheritance ---------")


class A:
    def m1(self):
        print("In A")


class B:
    def m2(self):
        print("In B")


class C(A, B):
    def m3(self):
        print("In C")


c = C()
c.m3()
c.m1()
c.m2()

print(C.mro())


class Father:
    def m1(self):
        print("Father : m1()")


class Mother:
    def m2(self):
        print("Mother : m2()")


class Son(Mother, Father):
    def m3(self):
        print("Son  : m3()")


s = Son()
s.m3()
s.m1()
s.m2()

# MRO  Method Resolution Order
'''
     Father     Mother
        m1()       m1()

            Son 
'''


class Father:
    def m1(self):
        print("Father : m1()")


class Mother:
    def m1(self):
        print("Mother : m2()")


class Son(Father, Mother):
    def m3(self):
        print("Son  : m3()")

    '''
    def m1(self):
        print("Son  : m1()")
    '''


s = Son()
s.m3()
s.m1()
print(Son.mro())

'''
    Animal :
      move():

    Cat         Dog           Snake      Tiger        
    move():      move():    move():    move():

# Normal Class
 For a method ( m1() ), the impl. is common for all sub classes

# Abstract class
Few methods need to be implemented in common way for all sub classes 
Other methods need to be implemented in unique way for all sub classes 

# Interface
For a method ( m1() ), the impl. is unique  for each sub class

'''

print("..................................................................")


# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Paa1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Paa2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def print_str(self):
        print(self.str1, self.str2)


ob = Derived()
ob.print_str()
