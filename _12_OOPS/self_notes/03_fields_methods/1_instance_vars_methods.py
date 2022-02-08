"""
Instance variables
Instance methods
"""


def function_1():
    print("This is function1 body ")


function_1()


class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables
    # State
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # Behaviour
    def get_edata(self):
        print("Employee Details :", self.eid, self.name, self.sal)


emp1 = Employee(1001, "Ali Hussain ", 20000)
emp1.get_edata()

emp2 = Employee(143, "Green Hulk ", 90000)
emp2.get_edata()

print(".............................")


class Shark:
    animal_type = "fish"


new_shark = Shark()
print(new_shark.animal_type)

print("............................")


class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5


new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)

print("........................................")


class Shark:
    # Class variables
    animal_type = "fish"
    location = "ocean"

    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method with instance variable followers
    def set_data(self):
        print("Shark Data :", self.name, self.age)


new_shark = Shark('Gold Fish', 100)
new_shark.set_data()
print(new_shark.animal_type)
print(new_shark.location)

print(".......................................................")


class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Name:', self.name, 'Age:', self.age)


# create first object
print('First Student')
emma = Student("Jessa", 14)
# call instance method
emma.show()

# create second object
print('Second Student')
kelly = Student("Kelly", 16)
# call instance method
kelly.show()

# create second object
print('Third Student')
ali = Student("Ali", 24)
# call instance method
ali.show()
