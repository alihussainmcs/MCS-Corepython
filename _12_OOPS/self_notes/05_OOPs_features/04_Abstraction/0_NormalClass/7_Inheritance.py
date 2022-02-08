
class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


# Create a child class that inherits from Parent
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.child_attribute = 'I am a child'


# Create instance of child
child = Child()

# Show attributes and methods of child class

print(child.child_attribute)

print(child.parent_attribute)

child.parent_method()


print("..............................................")


# inheritance


# Base class or Parent class
class Child:

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is student
    def isStudent(self):
        return False


# Derived class or Child class
class Student(Child):

    # True is returned
    def isStudent(self):
        return True


# An Object of Child
std = Child("Ali")
print(std.getName(), std.isStudent())

# An Object of Student

std = Student("Hulk")
print(std.getName(), std.isStudent())
