# Positional arguments

class Employee:
    # Parameterized Constructor
    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_edata(self):
        pass


ali = Employee(201, 'ILA', 20000)

'''
# Defining Constructor
    - Default constructor
    - Parameterized constructor
            - Positional arguments
            - Default arguments
            - keyword arguments

'''


# Default arguments example_1


class Employee:
    # parameterized constructors
    def __init__(self, eid=None, name=None, sal=None):  # Constructor overloading
        self.eid = eid
        self.name = name
        self.sal = sal

    def get_edata(self):
        print("Employee info : ", self.eid, self.name, self.sal)


ail = Employee()
ail.get_edata()

lai = Employee(201)
lai.get_edata()

chandra = Employee(201, 'Chandra')
chandra.get_edata()

ila = Employee(200, 'ILA', 10000)
ila.get_edata()

ALI = Employee(name='ALI', sal=20000)
ALI.get_edata()

print("...............................................................")


class Student:
    # Constructor - parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name

    def show(self):
        print("Hello", self.name)


student = Student("Ali")
student.show()

print("........................................")


class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

        # creates the object of the class Student


s = Student("ali", 101, 24)

# prints the attribute name of the object s
print(getattr(s, 'name'))

# reset the value of attribute age to 23
setattr(s, "age", 23)

# prints the modified value of age
print(getattr(s, 'age'))

# prints true if the student contains the attribute with name id

print(hasattr(s, 'id'))
# deletes the attribute age
delattr(s, 'age')

# this will give an error since the attribute age has been deleted
# print(s.age) AttributeError: 'Student' object has no attribute 'age'


print("....................................................................")


class Demo:
    def __init__(self, age, country):
        self.age = age
        self.place = country

    def hello(self):
        print(f"Hello, I am a {self.age} years old from {self.place}")


d = Demo(24, 'India')

d.hello()
