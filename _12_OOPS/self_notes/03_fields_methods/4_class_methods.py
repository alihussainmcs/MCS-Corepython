"""
class Class:
    pass
    # STATE
        # ==> Fields(1,2)  which represents data

        1. Class variables
        2. Instance variables
        3. local variables

    # BEHAVIOR
        # ==> Methods which represents implementation

       1. Class Method
       2. Instance Method
       3. Static method
"""

# Get employee count at a given point of time.


class Employee:
    comp = "MCS"  # sharing
    emp_count = 0  # Sharing + modifying

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.emp_count += 1

    # instance method(can access instance,class variables)
    def get_edata(self):
        print("Employee Info :", self.eid, self.name, self.sal)

    @classmethod
    def get_ecount(cls):
        print("Employee Count :", cls.comp, cls.emp_count)


Employee.get_ecount()

ali = Employee(101, 'Ali Hussain', 10000)
ali.get_edata()  # instance method ==> Employee.get_edata(ali)
Employee.get_ecount()  # class method    ==> Employee.get_ecount(Employee)


# To call class method, we can call using object,But don't do it.
# ali.get_ecount()

jay = Employee(101, 'Jayden  Chowder A', 20000)
jay.get_edata()
Employee.get_ecount()

moan = Employee(102, 'Moan Kumar', 45000)
moan.get_edata()
Employee.get_ecount()

'''
b tech : stu_id, name, marks ==> instance variables
        college name        ==> class variables(share)
        attendance          ==> class variable (share+Modify)


employees : eid,name,sal   Instance vars  UNIQUE(INDIVIDUAL DATA)
            comp_name      class vars     SHARABLE to all employees
            emp_count      class vars     SHARABLE + MODIFY
            attendance     class vars     SHARABLE + MODIFY 



class variables    : data which is sharable to all objects
                     data which is SHARE + MODIFY actions
class methods      : 1. To act only on class variables


instance variables : data is unique for each object 
instance methods   : 1. To act only on instance variables OR 
                     2. Both instance and class variables



CV   - ClassMethod, InstanceMethod 
IV   - InstanceMethod

'''

print(".............................................")

# Python program to demonstrate
# use of a class method and static method.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    def display(self):
        print("Name : ", self.name, "and Age : ", self.age)


person = Person('Ali', 24)
person.display()


print(".......................................")
# Python program to demonstrate
# use of a class method and static method.
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a
    # Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('Ali', 25)
person2 = Person.fromBirthYear('Alien', 1997)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(22))
