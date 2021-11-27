"""
@classmethod
@staticmethod

Decorator : Provides additional functionality for class or method/function
"""

"""
Decorators in Python

Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function
or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, 
without permanently modifying it.

First Class Objects
In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.

Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
Consider the below examples for better understanding.
Example 1: Treating the functions as objects.
"""


# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))
print("-------------------------------------------------------------")
"""
In the above example, we have assigned the function shout to a variable. This will not call the function instead it 
takes the function object referenced by a shout and creates a second name pointing to it, yell.

Example 2: Passing the function as an argument
"""


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)
print("-------------------------------------------------------------")

"""
In the above example, the greet function takes another function as a parameter (shout and whisper in this case). The 
function passed as an argument is then called inside the function greet.

Example 3: Returning functions from another functions.
"""


# Python program to illustrate functions
# Functions can return another function
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))
"""
In the above example, we have created a function inside of another function and then have returned the function created 
inside.
The above three examples depict the important concepts that are needed to understand decorators. 
"""
