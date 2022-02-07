"""
3. class variable:

A Python class variable is shared by all object instances of a class. They are
not defined inside any methods of a class. ... Because a class variable is
shared by instances of a class, the Python class owns the variable. As a result,
all instances of the class will be able to access that variable.

Class variables are declared when a class is being constructed.
Class variables are shared by all instances that access the class.

Class Variables are declared inside the construction of class. Since these
variables are owned by the class itself, they are shared by all class instances.
They, therefore, will usually have the equivalent value for each instance unless
we are utilizing the class variable in order to initialize a variable.

Class Variables are defined outside of all the methods by convention, classically
placed right under the header class and before the method of constructor and other functions.

#syntax:
# defining the class
class Class_name:
    # declaring the variable in the class
    var = "xyz"

#example:
# defining a class
class Animal:
    # declaring the class variable
    Terrestrial = "Lion"
# instantiating the class
my_Animal = Animal()
# printing the values
print("Name of the Animal:", my_Animal.Terrestrial)

#EXAMPLE:

class Espresso:
	menu_type = "Drink"

In this example, we declare a class variable called menu_type.
This class variable is assigned to the class Espresso.

Class variables are useful because they allow you to declare a variable when a
class has been built, which can then be used later in your class.

Like regular variables, class variables can store data of any type. So, we could
 store a Python dictionary, a Python tuple, or a Python list in a class variable.

3.1:Accessing a Class Variable in Python:

 we can access it when we create an object of our class. So, if we want to create
 a new class instance and see the value of the menu_type variable

#EXAMPLE:

class Espresso:
	menu_type = "Drink"

espresso_order = Espresso()
print(espresso_order.menu_type)

 we first define a class that has one class variable: menu_type. Then, we create
an instance of our class. This instance is called espresso_order.

In order to see the value of the menu_type variable in our class, we use the dot
notation. This is the name of the class followed by a period. Then, we specify
the name of the class variable you want to read.
Because our class variable is associated with a class, we don’t even need to
declare an instance of our class to see its value.

#EXAMPLE:

class Espresso:
	menu_type = "Drink"

print(Espresso.menu_type)

There are two main types: class variables, which have the same value across all
class instances (i.e. static variables), and instance variables, which have
different values for each object instance.

#SYNTAX:

class ClassName(object):
  class_variable = value #value shared across all class instances

  def __init__(instance_variable_value):
    self.instance_variable = instance_variable_value #value specific to instance. Instance variables are usually
    initialized in methods

#accessing instance variable
class_instance = ClassName()
class_instance.instance_variable

#accessing class variable
ClassName.class_variable
class_instance.class_variable


"""