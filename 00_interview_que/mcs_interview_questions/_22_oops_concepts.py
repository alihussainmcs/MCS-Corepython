"""
22.oops concept:

Python is also an object-oriented language since its beginning. It allows us to develop applications
using an Object-Oriented approach. In Python, we can easily create and use classes and objects.

An object-oriented paradigm is to design the program using classes and objects. The object is related
to real-word entities such as book, house, pencil, etc. The oops concept focuses on writing the
reusable code. It is a widespread technique to solve the problem by creating objects.

Major principles of object-oriented programming system are given below.

    1.Class
    2.Object
    3.Method
    4.Inheritance
    5.Polymorphism
    6.Data Abstraction
    7.Encapsulation

1.Class:
The class can be defined as a collection of objects. It is a logical entity that has some specific
attributes and methods. For example: if you have an employee class, then it should contain an attribute
and method, i.e. an email id, name, age, salary, etc.


Syntax

class ClassName:
        <statement-1>
        .
        .
        <statement-N>

2.Object:

The object is an entity that has state and behavior. It may be any real-world object like the mouse,
keyboard, chair, table, pen, etc.

Everything in Python is an object, and almost everything has attributes and methods. All functions
have a built-in attribute __doc__, which returns the docstring defined in the function source code.

When we define a class, it needs to create an object to allocate the memory. Consider the following
example.

#Example:

class car:
    def __init__(self,modelname, year):
        self.modelname = modelname
        self.year = year
    def display(self):
        print(self.modelname,self.year)

c1 = car("Toyota", 2016)
c1.display()


3.Method:

The method is a function that is associated with an object.
In Python, a method is not unique to class instances. Any object type can have methods.

4.Inheritance:

Inheritance is the most important aspect of object-oriented programming, which simulates the real-world
concept of inheritance. It specifies that the child object acquires all the properties and behaviors of
the parent object.

By using inheritance, we can create a class which uses all the properties and behavior of another class.
The new class is known as a derived class or child class, and the one whose properties are acquired is
known as a base class or parent class.

It provides the re-usability of the code.

5.Encapsulation:

Encapsulation is also an essential aspect of object-oriented programming. It is used to restrict access
to methods and variables. In encapsulation, code and data are wrapped together within a single unit from
being modified by accident.

6.Data Abstraction:

Data abstraction and encapsulation both are often used as synonyms. Both are nearly synonyms because
data abstraction is achieved through encapsulation.

Abstraction is used to hide internal details and show only functionalities. Abstracting something
means to give names to things so that the name captures the core of what a function or a whole
program does.



Index	        Object-oriented Programming	                Procedural Programming

1.	        Object-oriented programming is the
            problem-solving approach and used
            where computation is done by using
            objects.	                                Procedural programming uses a list of
                                                        instructions to do computation step by step.

2.	       It makes the development and maintenance
           easier.	                                    In procedural programming, It is not easy to
                                                        maintain the codes when the project becomes
                                                        lengthy.

3.	     It simulates the real world entity.
         So real-world problems can be easily solved
         through oops.	                                It doesn't simulate the real world. It works on
                                                        step by step instructions divided into
                                                         small parts called functions.


4.	    It provides data hiding. So it is more secure
        than procedural languages. You cannot access
        private data from anywhere.	                     Procedural language doesn't provide any proper
                                                         way for data binding, so it is less secure.

5.	   Example of object-oriented programming languages
       is C++, Java, .Net, Python, C#, etc.            	Example of procedural languages are: C, Fortran,
                                                        Pascal, VB etc.

7.Polymorphism:

The word polymorphism means having many forms. In programming, polymorphism means the same function
name (but different signatures) being used for different types.

#example:

# Python program to demonstrate in-built poly-
# morphic functions

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))

#method overloading:

Method Overloading is an example of Compile time polymorphism. In this, more than one method of the
same class shares the same method name having different signatures. Method overloading is used to
add more to the behavior of methods and there is no need of more than one class for method overloading.

Note: Python does not support method overloading. We may overload the methods but can only use the
latest defined method.

#example:

# Function to take multiple arguments
def add(datatype, *args):

	# if datatype is int
	# initialize answer as 0
	if datatype =='int':
		answer = 0

	# if datatype is str
	# initialize answer as ''
	if datatype =='str':
		answer =''

	# Traverse through the arguments
	for x in args:

		# This will do addition if the
		# arguments are int. Or concatenation
		# if the arguments are str
		answer = answer + x

	print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

#method overriding:

Method overriding is an example of run time polymorphism. In this, the specific
implementation of the method that is already provided by the parent class is provided
by the child class. It is used to change the behavior of existing methods and there is
a need for at least two classes for method overriding. In method overriding, inheritance
always required as it is done between parent class(superclass) and child class(child class) methods.

#example:


class A:

	def fun1(self):
		print('feature_1 of class A')

	def fun2(self):
		print('feature_2 of class A')


class B(A):

	# Modified function that is
	# already exist in class A
	def fun1(self):
		print('Modified feature_1 of class A by class B')

	def fun3(self):
		print('feature_3 of class B')


# Create instance
obj = B()

# Call the override function
obj.fun1()


S.NO	            Method Overloading	                        Method Overriding


1.	            In the method overloading, methods or
                functions must have the same name and
                different signatures.	                      Whereas in the method overriding, methods
                                                              or functions must have the same name and
                                                              same signatures.

2.	          Method overloading is a example of compile
              time polymorphism.	                          Whereas method overriding is a example of
                                                              run time polymorphism.

3.	          In the method overloading, inheritance may
              or may not be required.	                       Whereas in method overriding, inheritance
                                                                always required.

4.	          Method overloading is performed between methods
              within the class.	                                Whereas method overriding is done between
                                                                parent class and child class methods.

5.	        It is used in order to add more to the behavior
            of methods.                                     	Whereas it is used in order to change the
                                                                behavior of exist methods.

6.	       In method overloading, there is no need of more
           than one class.	                                     Whereas in method overriding, there is
                                                                need of at least of two classes.

                                                                
"""