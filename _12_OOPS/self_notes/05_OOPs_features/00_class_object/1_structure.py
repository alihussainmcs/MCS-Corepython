"""
Student
------------
 IV : r_no name   marks   percentage   section   fee    student_address

 CV : school_name school_address student_count


Instance variable : Individual to each object
Class variable : Sharable and modifiable by all objects


CV  ----> CM
IV  ----> IM

CV  ----> IM  Correct
IV  ----> CM  XXX

"""
'''
STATE 
 - Fields
    - Class variables 
    - Instance variables 

BEHAVIOR
 - Methods
    - Class method
    - Instance method
    - Static method

STATE  - BEHAVIOR
Fields - Methods

OOPs concepts:
--------------------
Class Object
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction


Encapsulation :  Binding the data members and 
                             member methods into single entity
                - data members   ==> fields
                - member methods ==> methods
                Ex: Class, object

                             Logical     Physical 
                    Class    Fields      Methods
                    object   Methods     Fields

Abstraction    : Hiding implementation details and exposing only method signature 

Abstraction   :      Class          -  0% abstraction
                     Abstract class -  0% to 100% abstraction
                     Interface      - 100%  abstraction 
'''

'''
class,object

1. Encapsulation :
-----------------
Definition: Binding the data members & member methods into single entity

entity         : class/object
data members   : Fields/Variables/Attributes  (class,instance variables)
member methods : Methods (Instance Methods,Class Methods,Static Methods)

ali = Employee(100,'Ali H, 15000)

Class  ===> Logical  -- DATA    Physical -- METHODS
Object ===> Physical -- DATA    Logical  -- METHODS (Through method access)

Ex : class is an example for encapsulation
     object is also an example


ali = Employee1(100,"AliH",15000)

2. Abstraction :
---------------
Hiding the implementation details in the methods of  a class

In a "Normal class" Abstraction is 0%        # all concrete methods
In "Abstract Class" Abstraction is 0-100 %   # 1. all concrete methods,
                                               2. all abstract methods
                                               3. Comb of concrete+abstract methods
In an "Interface"   Abstraction is 100%      # all abstract methods

During inheritance : Normal class,

3. Inheritance :
---------------
super class, sub class mechanism

4. Polymorphism :
---------------
    - Static Polymorphism  -- Method overloading
    - Dynamic Polymorphism -- Method overriding

'''

'''
 1. Class Defined and provided special method i.e, 
   __init__(constructor) method to initialize instance variables, 
    define respective methods to get the BEHAVIOR
2.  Create object for the respective class.
        Internally 
         Python creates empty object for us,and gives reference to self parameter
         Remaining parameters, we are passing the arguments
         In empty object, instance variables will be initialized with the given data
3. Finally whole object reference will be given to LHS
4. We can perform method calls using created object       
'''

'''
class var                  instance var
-------------------------- ----------------------------
while loading class        at the time of object creation

class var                  instance var
class methods              instance methods

instance variables cant be used inside class method**

++ Within instance methods we can use class variables*****
vice versa is not True ==> within class methods we can't use instance variables
'''


class Employee:
    """This class give details about employee"""

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_data(self):
        print("Employee data : ", self.eid, self.name, self.sal)


# Built in class attributes '''


print("Employee.__dict__:", Employee.__dict__)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)

# CRUD - Create Retrieve Update Delete

ali = Employee(100, "ILA", 10000)  # CREATE

'''
setattr : To set IV value inside object  # UPDATE
getattr : To retrieve IV value           # RETRIEVE 
hasattr : To check IV has specific value # RETRIEVE
delattr : To delete IV                   # DELETE   
'''
# getter - RETRIEVE
print("ali name :", getattr(ali, "name"))
print("ali eid  :", getattr(ali, "eid"))
# print("Madhu addr  :", getattr(ali, "addr")) AttributeError: 'Employee' object has no attribute 'addr'

# setter - UPDATE
print("Setting name :", setattr(ali, "name", "MAD"))
print("Setting eid  :", setattr(ali, "eid", 200))
print("Setting addr :", setattr(ali, "address", 'Bangalore'))

print("Get name:", getattr(ali, "name"))
print("Get eid :", getattr(ali, "eid"))
print("Get addr:", getattr(ali, "address"))

print("Has attr sal :", hasattr(ali, "sal"))
print("Has attr addr:", hasattr(ali, "address"))

print("Delete attr :", delattr(ali, "sal"))
# print(getattr(ali, "sal")) AttributeError: 'Employee' object has no attribute 'sal'

print("..................................................")


class Phone:
    username = "Ali"  # public variable
    __how_many_times_turned_on = 6  # private variable

    def call(self):  # public method
        print("Ring-ring!")
        self.__turn_on()

    def __turn_on(self):  # private method
        self.__how_many_times_turned_on += 1
        print("Times was turned on: ", self.__how_many_times_turned_on)


my_phone = Phone()

my_phone.call()
print("The username is ", my_phone.username)

print("................................")


class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    # private static method
    @staticmethod
    def __updateSoftware():
        print('updating software')


red_car = Car()
red_car.drive()

print("..............................................")


class Car:
    __max_speed = 0
    __name = ""

    def __init__(self):
        self.__max_speed = 100
        self.__name = "Supercar"

    def drive(self):
        print('driving. max_speed ' + str(self.__max_speed))


red_car = Car()
red_car.drive()
red_car.__max_speed = 10  # will not change variable because its private
red_car.drive()


print(".............................................")


class Car:
    __max_speed = 0
    __name = ""

    def __init__(self):
        self.__max_speed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. max_speed ' + str(self.__max_speed))

    def setMaxSpeed(self, speed):
        self.__max_speed = speed


red_car = Car()
red_car.drive()
red_car.setMaxSpeed(320)
red_car.drive()
