"""
2. what is static variable:?

Class or Static Variables in Python:

Class or Static variables are the variables that belong to the class and not to objects.
Class or Static variables are shared amongst objects of the class. All variables which
are assigned a value in the class declaration are class variables. And variables which
are assigned values inside class methods are instance variables.

                        (AND)
When we declare a variable inside a class, but outside the method, it is called
a static or class variable. It can be called directly from a class but not through
the instances of a class. However, the static variables are quite different from
the other member, and it does not conflict with the same variable name in the Python program.

#example:

class Shape:
    # class or static variable
    cat = 'Geometrical'

    def __init__(self, type):
        # instance variable
        self.typ = type

    # method to show data
    def show(self):
        # accessing class variable
        print('Shape is of category: ', Shape.cat)
        # accessing instance variable
        print('And shape is: ', self.type)


tr = Shape('Triangle')
sq = Shape('Square')
rec = Shape('Circle')

tr.show()
sq.show()
rec.show()


In the above program, cat is a class variable because it is defined outside of
all the class methods and inside the class definition and type is an instance
variable as it is defined inside a method.

2.1:Points to Remember about static variable and methods:

Following are some important take away:

    1.Static variable and methods are used when we want to define some behaviour or
    property specific to the class and which is something common for all the class objects.

    2.If you look closely, for a static method we don't provide the argument self
    because static methods don't operate on objects.

We can directly access a static variable in Python using the same class object
with a dot operator

#example:
class Car:
    # define the class variable or static variable of class Car
    num = 7
    msg = 'This is a good Car.'

# create the object of the class
obj = Car()

# Access a static variable num using the class name with a dot operator.
print ("Lucky No.", Car.num)
print (Car.msg)



3.Static Method:

Python has a static method that belongs to the class. It is just like a static
variable that bounds to the class rather than the class's object. A static method
can be called without creating an object for the class. It means we can directly
call the static method with the reference of the class name. Furthermore, a static
method is constrained with a class; hence it cannot change the state of an object.

3.1:Features of static methods:

1.A static method in Python related to the class.
2.It can be called directly from the class by reference to a class name.
3.It cannot access the class attributes in the Python program.
4.It is bound only to the class. So it cannot modify the state of the object
5.It is also used to divide the utility methods for the class.
6.It can only be defined inside a class but not to the objects of the class.
7.All the objects of the class share only one copy of the static method.


3.2:There are the two ways to define a static method in Python:

    1.Using the staticmethod() Method
    2.Using the @staticmethod Decorator

A staticmethod() is a built-in function in Python that is used to return a
given function as a static method.

#syntax:

staticmethod (function)

A staticmethod() takes a single parameter. Where the passed parameter is a
function that needs to be converted to a static method.

#example:
class Marks:
    def Math_num(a, b): # define the static Math_num() function
        return a + b

    def Sci_num(a, b): # define the static Sci_num() function
        return a +b

    def Eng_num(a, b):  # define the static Eng_num() function
        return a +b
# create Math_num as static method
Marks.Math_num = staticmethod(Marks.Math_num)

# print the total marks in Maths
print (" Total Marks in Maths" , Marks.Math_num(64, 28))

# create Sci_num as static method
Marks.Sci_num = staticmethod(Marks.Sci_num)

# print the total marks in Science
print (" Total Marks in Science" , Marks.Sci_num(70, 25))

# create Eng_num as static method
Marks.Eng_num = staticmethod(Marks.Eng_num)

# print the total marks in English
print (" Total Marks in English" , Marks.Eng_num(65, 30))



to access the static method of the class using the @staticmethod in Python.
#example:
class Test:
    # define a static method using the @staticmethod decorator in Python.
    @staticmethod
    def beg():
        print ("Welcome to the World!! ")

# create an  object of the class Test
obj = Test()
# call the static method
obj.beg()


3.3:Function returns a value using the static method:

#example:
class Person:
    @staticmethod
    def Age (age):
        if (age <= 18): # check whether the Person is eligible to vote or not.
            print ("The person is not eligible to vote.")
        else:
            print ("The person is eligible to vote.")

Person.Age(17)

"""