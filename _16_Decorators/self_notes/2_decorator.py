"""
Decorators
As stated above the decorators are used to modify the behaviour of function or class. In Decorators, functions are taken
as the argument into another function and then called inside the wrapper function.
Syntax for Decorator:

@mcs_decorator
def hello_decorator():
    print("MCS")


'''Above code is equivalent to -

def hello_decorator():
    print("MCS")

hello_decorator = mcs_decorator(hello_decorator)'''

In the above code, gfg_decorator is a callable function, will add some code on the top of some another callable
function, hello_decorator function and return the wrapper function.
Decorator can modify the behaviour:

"""


# defining a decorator
def hello_decorator(func):
    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()

print("---------------------------------------------------------------------------")

# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num_1):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num_1))


# calling the function.
factorial(5)

print("--------------------------------------------------------------------")


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a_1, b_1):
    print("Inside the function")
    return a_1 + b_1


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))
print("-----------------------------------------------------------------------------------")

"""
In the above example, you may notice a keen difference in the parameters of the inner function. The inner function takes
the argument as *args and **kwargs which means that a tuple of positional arguments or a dictionary of keyword arguments
can be passed of any length. This makes it a general decorator that can decorate a function having any number of 
arguments.


Chaining Decorators
In simpler terms chaining decorators means decorating a function with multiple decorators.
Example:
"""


# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())

# The above example is similar to calling the function as     --–>     decor1(decor(num))
