"""
Apply hike based on rating on a scale of 5.
If rating is 4 to 5 - 30%
             3 to 4 - 20%
             2 to 3 - 10%
             <2     -  no hike
"""


# Class


class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee Data :", self.eid, self.name, self.sal)

    def apply_hike(self, rating):
        print("Employee Hike with rating ", rating)
        if 4 <= rating <= 5:
            hike = self.sal * 0.3
            print("Hike is :", hike)
        elif 3 <= rating < 4:
            hike = self.sal * 0.2
            print("Hike is :", hike)
        elif 2 <= rating < 3:
            hike = self.sal * 0.1
            print("Hike is :", hike)
        else:
            print("No Hike ! ")


ali = Employee(1001, "Ali K", 20000)
ali.get_edata()

val = 5  # int(input("Enter your rating :"))
Employee.apply_hike(ali, val)
print("-------------------------------")

hulk = Employee(1002, "Green Hulk", 30000)
hulk.get_edata()

val = 4  # int(input("Enter your rating :"))
hulk.apply_hike(val)  # Employee.apply_hike(hulk, val)
# hulk.apply_hike(hulk, val) TypeError: apply_hike() takes 2 positional arguments but 3 were given

print("......................................................")


class Shape:

    # Calling Constructor
    def __init__(self, edge, color):
        self.edge = edge
        self.color = color

    # Instance Method
    def finEdges(self):
        return self.edge

    # Instance Method
    def modifyEdges(self, new_edge):
        self.edge = new_edge


circle = Shape(0, 'red')
square = Shape(4, 'blue')

# Calling Instance Method
print("No. of edges for circle: ", circle.finEdges())

# Calling Instance Method
square.modifyEdges(6)

print("No. of edges for square: ", square.finEdges())

print(".......................................")


class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

        # Sample Method

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Ali')
p.say_hi()

print("..................................................")


class Student:
    def __init__(self, roll_no, name, age):
        # Instance variable
        self.roll_no = roll_no
        self.name = name
        self.age = age

    # instance method access instance variable
    def show(self):
        print('Roll Number:', self.roll_no, 'Name:', self.name, 'Age:', self.age)

    # instance method to modify instance variable
    def update(self, roll_number, age):
        self.roll_no = roll_number
        self.age = age


# create object
print('class VIII')
stud = Student(20, "Emma", 14)
# call instance method
stud.show()

# Modify instance variables
print('class IX')
stud.update(35, 15)
stud.show()
