"""
1. what is instance variable?

If the value of a variable varies from object to object, then such variables are
called instance variables. For every object, a separate copy of the instance variable
will be created. Instance variables are not shared by objects.
Every object has its own copy of the instance attribute.
This means that for each object of a class, the instance variable value is different.


#example:
Class Test:
    def __init__(self,num):
            self.num=num #instance variable
t1=Test(10)
t2=Test(20)
t3=Test(30)
 every object has its own copy of instance variable

1.1:Create Instance Variables:

Instance variables are declared inside a method using the self keyword. We use
a constructor to define and initialize the instance variables.

class Student:
    # constructor
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age

# create first object
s1 = Student("Jessa", 20)

# access instance variable
print('Object 1')
print('Name:', s1.name)
print('Age:', s1.age)

# create second object
s2= Student("Kelly", 10)

# access instance variable
print('Object 2')
print('Name:', s2.name)
print('Age:', s2.age)


#Note:

When we created an object, we passed the values to the instance variables using a constructor.
Each object contains different values because we passed different values to a constructor
to initialize the object.Variable declared outside __init__() belong to the class.
They’re shared by all instances.


1.2:Ways to Access Instance Variable:

There are two ways to access the instance variable of class:

    1.Within the class in instance method by using the object reference (self)
    2.Using getattr() method

"""
