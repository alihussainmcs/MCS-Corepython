"""


Python: AttributeError
Last Updated : 09 Aug, 2021
In every programming language, if we develop new programs, there is a high chance of getting errors or exceptions.
These errors yield to the program not being executed. One of the error in Python mostly occurs is “AttributeError”.
AttributeError can be defined as an error that is raised when an attribute reference or assignment fails.
For example, if we take a variable x we are assigned a value of 10. In this process suppose we want to append another
value to that variable. It’s not possible. Because the variable is an integer type it does not support the append
method. So in this type of problem, we get an error called “AttributeError”. Suppose if the variable is list type
then it supports the append method. Then there is no problem and not getting”Attribute error”.

Note: Attribute errors in Python are generally raised when an invalid attribute reference is made.
There are a few chances of getting AttributeError.

"""
# AttributeError

# x = 10

# Raises an AttributeError
# x.append(6)  # AttributeError: 'int' object has no attribute 'append'

# Raises an AttributeError as there is no
# method as fst for strings
# string = "The famous  movie is { }".fst("ali")  AttributeError: 'str' object has no attribute 'fst'
# print(string)


def attribute_error(a):
    try:
        a.append(1)
        print(a)
    except AttributeError as atr:
        print(atr)


attribute_error([10])
attribute_error(10)
attribute_error(12.8)
attribute_error(True)
attribute_error(10j)
attribute_error('a')





