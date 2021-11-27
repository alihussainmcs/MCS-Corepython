"""
Interview Questions
"""
# import builtins

'''
builtins.py
---------------
Functions:
---------------
all vs any  in python
abs
ascii vs bin vs chr  vs ord vs pow

dir() help()

eval vs exec vs exit

evaluate

input id print 
isinstance vs issubclass 
iter() vs next()
repr() vs str()

classes:
--------------
object
BaseException Exception
                    ArithmeticError 
int float long bool str list tuple dict set 

Access modifiers: public private protected default

getdata() : public 
_getdata() : protected
__getdata() : private 

'''

# builtins.help()

print("......................  all vs any ..............................")
"""
Any-------
Returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of as a 
sequence of OR operations on the provided iterables.
It short circuit the execution i.e. stop the execution as soon as the result is known.

Syntax : any(list of iterables)
"""
print("...........    any     ...................")
# Since all are false, false is returned
print(any([False, False, False, False]))

# Here the method will short-circuit at the
# second item (True) and will return True.
print(any([False, True, False, False]))

# Here the method will short-circuit at the
# first (True) and will return True.
print(any([True, False, False, False]))

"""
All
Returns true if all of the items are True (or if the iterable is empty). All can be thought of as a sequence of 
AND operations on the provided iterables. It also short circuit the execution i.e. stop the execution as soon as 
the result is known.

Syntax : all(list of iterables)
"""
print("...........    all     ...................")

# Here all the iterables are True so all
# will return True and the same will be printed
print(all([True, True, True, True]))

# Here the method will short-circuit at the
# first item (False) and will return False.
print(all([False, True, True, False]))

# This statement will return False, as no
# True is found in the iterables
print(all([False, False, False]))

print(".........   example      .....................")
# This code explains how can we
# use 'any' function on list
list1 = []
list2 = []

# Index ranges from 1 to 10 to multiply
for i in range(1, 11):
    list1.append(4 * i)

# Index to access the list2 is from 0 to 9
for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)

print('See whether at least one number is divisible by 5 in list 1=>')
print(any(list2))
print(all(list2))

print(".................. abs        .......................")

"""
Python abs() function is used to return the absolute value of a number, 
i.e., it will remove the negative sign of the number.  

abs()
built - in function
"""

# floating point number
fl = -54.26
print('Absolute value of float is:', abs(fl))

# An integer
i = -94
print('Absolute value of integer is:', abs(i))

# A complex number
c = (3 - 4j)
print('Absolute value or Magnitude of complex is:', abs(c))

print("..............    ascii vs bin vs chr  vs ord vs pow       ..................")
"""
ascii() in Python
Python ascii() function returns a string containing a printable representation of an object and escapes the non-ASCII 
characters in the string.
"""
print("..................  ascii()        ...............................")
str_1 = "A ë l ê i * ?  H ? u s s"
print("String str_1 :", str_1)
print("String with ascii(str_1) :", ascii(str_1))

"""
bin() in Python
Python bin() function returns the binary string of a given integer.
"""
print(".................. bin()  ...............................")

# declare variable
num = 100

# print binary number
print("Number :", num)
print('Number in binary format :', bin(num))

print("............... chr()   ...................")
"""
chr() in Python
The chr() method returns a string representing a character whose Unicode code point is an integer.
Syntax:
chr(num)
num : integer value
"""

# chr() builtin function

numbers = [65, 76, 73]

for number in numbers:
    # Convert ASCII-based number to character.
    letter = chr(number)
    print("Character of ASCII value", number, "is ", letter)

print("............... 2nd ex..............................")
print('chr(1) :', chr(1))
print('chr(10) :', chr(10))
print('chr(100) :', chr(100))
print('chr(200) :', chr(200))
print('chr(300) :', chr(300))
print('chr(400) :', chr(400))
print('chr(500) :', chr(500))
print('chr(600) :', chr(600))
print('chr(700) :', chr(700))
print('chr(800) :', chr(800))
print('chr(900) :', chr(900))
print('chr(1000) :', chr(1000))
print('chr(10000) :', chr(10000))

"""
ord() function in Python
Python ord() function returns the Unicode code from a given character. This function accepts a string of unit length 
as an argument and returns the Unicode equivalence of the passed argument. In other words, given a string of length 1, 
the ord() function returns an integer representing the Unicode code point of the character when an argument is a 
Unicode object, or the value of the byte when the argument is an 8-bit string.

Python ord() syntax:
"""
print("........................ ord()   ...................................")
# integer representing the Unicode code
value = ord("A")
print('unicode value of ord("A") is :', value)

value1 = ord('L')
print('unicode value of ord("L") is :', value1)

value3 = ord('I')

# prints the unicode value
print('unicode value of ord("I") is :', value3)

# Raises Exception
# value1 = ord('AB')
# print(value1)  TypeError: ord() expected a character, but string of length 2 found

print(".....................  pow()        .............................")
"""
pow() in Python
Difficulty Level : Basic
Last Updated : 22 Sep, 2021
Python pow() function returns the power of the given numbers. This function computes x**y. This function first 
converts its arguments into float and then computes the power. 

Syntax: pow(x,y)

Parameters : 

x : Number whose power has to be calculated.
y : Value raised to compute power.
Return Value :  Returns the value x**y in float.

"""

print("The value of pow(5, 1) is : ", pow(5, 1))
print("The value of pow(5, 2) is : ", pow(5, 2))

print("The value of (5**2) % 10 ie pow(3, 4, 10) is : ", pow(3, 4, 10))
print("The value of (5**2) % 10 ie pow(3, 4, 10) is : ", pow(3, 4, 2))

print("            2nd ex                       ")
# and non-negative cases

# positive x, positive y (x**y)
print("Positive x=4 and positive y=3 : ", end="")
print(pow(4, 3))

print("Negative x=-4 and positive y=3 : ", end="")
# negative x, positive y (-x**y)
print(pow(-4, 3))

print("Positive x=4 and negative y=-3 : ", end="")
# positive x, negative y (x**-y)
print(pow(4, -3))

print("Negative x=-4 and negative y=-3 : ", end="")
# negative x, negative y (-x**-y)
print(pow(-4, -3))
print('----------------------------  dir() help()   -------------------------------------------')
"""
dir() function in Python

dir() is a powerful inbuilt function in Python3, which returns list of the attributes and methods of any object 
(say functions , modules, strings, lists, dictionaries etc.)
Syntax : 
        dir()
"""
print('------------------------------   dir()  ---------------------------------------------')
# when no parameters are passed

# Note that we have not imported any modules
print(dir())

# Now let's import two modules
import random
import math

# return the module names added to
# the local namespace including all
# the existing ones as before
print(dir())

print("-------------------------  help()   ----------------------------------")
"""
Help function in Python
The Python help function is used to display the documentation of modules, functions, classes, keywords, etc. 

The help function has the following syntax:
help([object])
Python help() function arguments
object: Call help of the given object.
If the help function is passed without an argument, then the interactive help utility starts up on the console.
"""
help(print)
print("**********************************************************************************8")


class Helper:
    def __init__(self):
        """The helper class is initialized"""

    @staticmethod
    def print_help():
        """Returns the help description"""
        print('helper description')


help(Helper)
print("==============================================================================")
help(Helper.print_help)

print('----------------------------  eval vs exec vs exit   -------------------------------------------')
print('----------------------------  eval  -------------------------------------------')
"""
eval in Python
Python eval() function parse the expression argument and evaluate it as a python expression and runs python 
expression(code) within the program.

Python eval() syntax

eval(expression, globals=None, locals=None)
Python eval() parameters
expression: this string is parsed and evaluated as a Python expression
globals (optional): a dictionary to specify the available global methods and variables.
locals (optional): another dictionary to specify the available local methods and variables.
"""

evaluate = 'x*(x+1)*(x+2)'
print(evaluate)
print(type(evaluate))

x = 3
print(type(x))

expression = eval(evaluate)
print(expression)
print(type(expression))

print('..................... 2nd ex. ..............................')

evaluate = 'x*(x+1)*(x+2)*(x-1)'
print(evaluate)
print(type(evaluate))

x = 3
print(type(x))

expression = eval(evaluate)
print(expression)
print(type(expression))

"""
exec() in Python

exec() function is used for the dynamic execution of Python program which can either be a string or object code. 
If it is a string, the string is parsed as a suite of Python statements which is then executed unless a syntax error 
occurs and if it is an object code, it is simply executed. We must be careful that the return statements may not be 
used outside of function definitions not even within the context of code passed to the exec() function. It doesn’t 
return any value, hence returns None. 
Syntax: 
        exec(object[, globals[, locals]])
"""
print('.............................  exec()   ........................................')

program = 'print("The sum of 5 and 10 is", (5+10))'
exec(program)
print('.............................  2nd ex.   ........................................')

# The math class is used to include all the
# math functions
from math import *

exec("print(dir())")

print('Python exit commands: quit(), exit(), sys.exit() and os._exit()')
"""
The functions quit(), exit(), sys.exit() and os._exit() have almost same functionality as they raise the SystemExit 
exception by which the Python interpreter exits and no stack traceback is printed.
We can catch the exception to intercept early exits and perform cleanup activities; if uncaught, the interpreter 
exits as usual.

When we run a program in Python, we simply execute all the code in file, from top to bottom. Scripts normally exit 
when the interpreter reaches the end of the file, but we may also call for the program to exit explicitly with the 
built-in exit functions.
"""
print('........................... quit() ..............................')
"""
quit()
It works only if the site module is imported so it should not be used in production code.Production code means the code
is being used by the intended audience in a real-world situation. This function should only be used in the interpreter.

It raises the SystemExit exception behind the scenes. If you print it, it will give a message:
"""
# quit()
'''
for i in range(10):

    # If the value of i becomes
    # 5 then the program is forced
    # to quit
    if i == 5:
        # prints the quit message
        print('quit')
        quit()
    print(i)
'''
"""
exit() is defined in site.py and it works only if the site module is imported so it should be used in the interpreter 
only. It is like a synonym of quit() to make the Python more user-friendly. It too gives a message when printed:
"""
'''
# exit()

for i in range(10):

    # If the value of i becomes
    # 5 then the program is forced
    # to exit
    if i == 5:
        # prints the exit message
        print('exit')
        exit()
    print(i)
'''

"""
sys.exit([arg])
Unlike quit() and exit(), sys.exit() is considered good to be used in production code for the sys module is always 
available. The optional argument arg can be an integer giving the exit or another type of object. If it is an integer,
 zero is considered “successful termination”.

Note: A string can also be passed to the sys.exit() method.

Example – A program which stops execution if age is less tha
"""
'''  
import sys
age = 19

if age < 18:

    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
'''
print('end of execution ............')

"""
os._exit(n)
os._exit() method in Python is used to exit the process with specified status without calling cleanup handlers, 
flushing stdio buffers, etc.

Note: This method is normally used in child process after os.fork() system call. The standard way to exit the process 
is sys.exit(n) method.
"""
'''
# Python program to explain os._exit() method

# importing os module
import os

# Create a child process
# using os.fork() method
pid = os.fork()

# pid greater than 0
# indicates the parent process
if pid > 0:

    print("\nIn parent process")
    # Wait for the completion
    # of child process and
    # get its pid and
    # exit status indication using
    # os.wait() method
    info = os.waitpid(pid, 0)

    # os.waitpid() method returns a tuple
    # first attribute represents child's pid
    # while second one represents 
    # exit status indication

    # Get the Exit code
    # used by the child process
    # in os._exit() method

    # firstly check if
    # os.WIFEXITED() is True or not
    if os.WIFEXITED(info[1]):
        code = os.WEXITSTATUS(info[1])
        print("Child's exit code:", code)

else:
    print("In child process")
    print("Process ID:", os.getpid())
    print("Hello ! Ali")
    print("Child exiting..")

    # Exit with status os.EX_OK
    # using os._exit() method
    # The value of os.EX_OK is 0
    os._exit(os.EX_OK)
'''

print("..................   input id print   .........................")

"""
Taking input in Python
Developers often have a need to interact with users, either to get data or to provide some sort of result. 
Most programs today use a dialog box as a way of asking the user to provide some type of input. While Python provides 
us with two inbuilt functions to read the input from the keyboard.

input ( prompt )


# Python program showing 
# a use of input()
  
val = input("Enter your value: ")
print(val)

"""

"""
id() function in Python

id() is an inbuilt function in Python.
Syntax:

id(object)

As we can see the function accepts a single parameter and is used to return the identity of an object. This identity 
has to be unique and constant for this object during the lifetime. Two objects with non-overlapping lifetimes may have 
the same id() value. If we relate this to C, then they are actually the memory address, here in Python it is the unique 
id. This function is generally used internally in Python.
"""
print('...................   id()   .............................................')
str1 = "ali"
print(id(str1))

str2 = "hulk"
print(id(str2))

# This will return True
print(id(str1) == id(str2))

# Use in Lists
list1 = ["sauna", "priya", "abdul"]
print(id(list1[0]))
print(id(list1[2]))

# This returns false
print(id(list1[0]) == id(list1[2]))

print('...................   print()   .............................................')
"""
Python | Output using print() function

Python print() function prints the message to the screen or any other standard output device.
Parameters: 

value(s) : Any value, and as many as you like. Will be converted to string before printed
sep='separator' : (Optional) Specify how to separate the objects, if there is more than one.Default :' ' 
end='end': (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
Returns: It returns output to the screen.

Though it is not necessary to pass arguments in the print() function, it requires an empty parenthesis at the end that 
tells python to execute the function rather calling it by name. Now, let’s explore the optional arguments that can be 
used with the print() function.

String Literals
String literals in python’s print statement are primarily used to format or design how a specific string appears when 
printed using the print() function.

\n : This string literal is used to add a new blank line while printing a statement.
'' : An empty quote ('') is used to print an empty line.
"""
print("Welcome to print function ............")

print(".........................   isinstance vs issubclass   ...............................")

"""
Python isinstance() method

Python isinstance() function returns True if the object is specified types, and it will not match then return False. 

Syntax : isinstance(obj, class)

Parameters : 

obj : The object that need to be checked as a part of class or not.
class : class/type/tuple of class or type, against which object is needed to be checked.
Returns : True, if object belongs to the given class/type if single class is passed or any of the class/type if 
tuple of class/type is passed, else returns False. Raises

TypeError: if anything other than mentioned valid class type. 
"""
print(".........................   isinstance   ...............................")

# working of isinstance()
# with native types

# initializing native types
test_int = 5
test_list = [1, 2, 3]

# testing with isinstance
print("Is test_int integer? : " + str(isinstance(test_int, int)))
print("Is test_int string? : " + str(isinstance(test_int, str)))
print("Is test_list integer? : " + str(isinstance(test_list, int)))
print("Is test_list list? : " + str(isinstance(test_list, list)))

# testing with tuple
print("Is test_int integer or list or string? : "
      + str(isinstance(test_int, (list, int))))

print(".........................  issubclass   ...............................")

"""
Python issubclass()

We know that inheritance is one of the building blocks of Object-Oriented Programming concept. It is the capability of 
one class to derive or inherit the properties from some other class. It also provides the re-usability of code. We don’t
have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.

Python issubclass()
Python issubclass() is built-in function used to check if a class is a subclass of another class or not. This function
returns True if the given class is the subclass of given class else it returns False.

Syntax: issubclass(object, class info)

Parameters:
Object: class to be checked
class info: class, types or a tuple of classes and types

Return Type: True if object is subclass of a class, or any element of the tuple, otherwise False.
"""


# Python program to demonstrate
# issubclass()


# Defining Parent class
class Vehicles:

    # Constructor
    def __init__(self):
        print('constructor of  vehicles............. ')


# Defining Child class
class Car(Vehicles):

    # Constructor
    def __init__(self):
        super().__init__()


print(issubclass(Car, Vehicles))
print(issubclass(Car, list))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicles)))

print("..............................  iter() vs next()   ................................")
print("..............................  iter()   ................................")

"""
Python iter() method

python iter() method returns the iterator object, it is used to convert an iterable to the iterator.

Syntax : iter(obj, sentinel)

Parameters : 
obj : Object which has to be converted to iterable ( usually an iterator ).
sentinel : value used to represent end of sequence.
Returns : Iterator object
Properties of Iterators
Iteration object remembers iteration count via internal count variable.
Once the iteration is complete, it raises a StopIteration exception and the iteration count cannot be reassigned to 0.
Therefore, it can be used to traverse the container just once.
"""
# working of iter()

# initializing list
lis1 = [1, 2, 3, 4, 5]

# printing type
print("The list is of type : " + str(type(lis1)))

# converting list using iter()
lis1 = iter(lis1)

# printing type
print("The iterator is of type : " + str(type(lis1)))

# using next() to print iterator values
print(next(lis1))
print(next(lis1))
print(next(lis1))

print("..............................  next()   ................................")
"""
Python next() method
Python next() function returns the next item of an iterator. In this article, we will cover next() syntax, next() 
parameters, next() returns.

Syntax : next(iter, stopdef)
Parameters : 
iter : The iterator over which iteration is to be performed.
stopdef : Default value to be printed if we reach end of iterator.
Returns : Returns next element from the list, if not present prints the default value. If default value is not present,
raises the StopIteration error.
"""
# Python code to demonstrate
# working of next()

# initializing list
list1 = [1, 2, 3, 4, 5]

# converting list to iterator
list1 = iter(list1)

print("The contents of list are : ")

# printing using next()
# using default
while 1:
    val = next(list1, 'end')
    if val == 'end':
        print('list end')
        break
    else:
        print(val)

print('...................  repr() vs str()  ..............................')
"""
str() and repr() both are used to get a string representation of object.
"""
s = 'Hello, ali.'
print(str(s))
print(str(2.0 / 11.0))

s = 'Hello, hulk.'
print(repr(s))
print(repr(2.0 / 11.0))

"""
From above output, we can see if we print string using repr() function then it prints with a pair of quotes and if we 
calculate a value we get more precise value than str() function.

Following are differences:

str() is used for creating output for end user while repr() is mainly used for debugging and development. repr’s goal 
is to be unambiguous and str’s is to be readable. For example, if we suspect a float has a small rounding error, repr 
will show us while str may not.
repr() compute the “official” string representation of an object (a representation that has all information about the 
object) and str() is used to compute the “informal” string representation of an object (a representation that is useful
 for printing the object).
The print statement and str() built-in function uses __str__ to display the string representation of the object while 
the repr() built-in function uses __repr__ to display the object.

"""

print(' --------------------  2nd ex. .......................')
import datetime

today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))

print("----------------      Access modifiers: public private protected default   --------------")

"""
Various object-oriented languages like C++, Java, Python control access modifications which are used to restrict access
to the variables and methods of the class. Most programming languages has three forms of access modifiers, which are 
Public, Protected and Private in a class.
Python uses ‘_’ symbol to determine the access control for a specific data member or a member function of a class. 
Access specifiers in Python have an important role to play in securing data from unauthorized access and in preventing 
it from being exploited.
A Class in Python has three types of access modifiers:
Public Access Modifier
Protected Access Modifier
Private Access Modifier
Public Access Modifier:
The members of a class that are declared public are easily accessible from any part of the program. All data members 
and member functions of a class are public by default. 
"""


# defining a class Employee


class Employee:
    # constructor
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal


emp = Employee("Ironman", 999000)

print('Salary of employee :', emp.sal)

"""
protected Access Modifier
According to Python convention adding a prefix _(single underscore) to a variable name makes it protected. Yes, 
no additional keyword required.
"""


# defining a class Employee
class Employee:
    # constructor
    def __init__(self, name, sal):
        self._name = name  # protected attribute
        self._sal = sal  # protected attribute


emp = Employee("Captain", 10000)
print('Salary of employee :', emp._sal)
"""
Similarly if there is a child class extending the class Employee then it can also access the protected member variables
of the class Employee. Let's have an example:
"""

"""
private Access Modifier
While the addition of prefix __(double underscore) results in a member variable or function becoming private.

# defining class Employee


class Employee:
    def __init__(self, name, sal):
        self.__name = name    # private attribute
        self.__sal = sal     # private attribute


emp = Employee("Bill", 1000000)
print(emp.__sal)
If we want to access the private member variable, we will get an error.
AttributeError: 'Employee' object has no attribute '__sal'
"""
