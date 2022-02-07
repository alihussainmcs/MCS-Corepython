"""
# Types
1. Predefined Functions   : print() id() type()   int float str list tuple dict set
2. User defined Functions : Programmer defined functions
"""

x = 101
"""
x  <==> variable 
101 <==> value
=  <==> Assignment operator 
"""

print("The value of x is :", x)

print('id of x :', id(x))

print('type of x :', type(x))


"""
Function definition syntax :    def <func_name> () :    # f(parameters)
                                  # def sum(n1, n2):    # f(x)   

n1,n2 are parameters not variables
"""

# Requirement : Sum of 2 given numbers
# A. With out functions

# I. STATE
a = 10
b = 20

# II. BEHAVIOR
sum_1 = a + b

print("Sum of given ", sum_1)

print("-----------Using functions--------")
# B. With Functions

# I. STATE
a = 10
b = 20


# II. Behaviour
# Function definition

def sum(n1, n2):  # function signature
    result = n1 + n2  # function body
    print("Addition is : ", result)

# Function calling


sum(a, b)
sum(101, 102)

"""
1. Function definition:
                                def sum(n1, n2):
                                    result = n1 + n2 
                                    print("Addition is : ", result)

    -   Function signature:
                                def sum(n1, n2):

    -  Function body/implementation
                                result = n1 + n2 
                                print("Addition is : ", result)

"""


# REQ : Subtraction of two numbers

# Without function

a = 21

b = 10

sub = a - b

print('Subtraction of numbers :', sub)

'''
Problem with above code -->
    
    Code can not re-used ie, suppose we want to subtract another two numbers then we will have to do same step again.
    This will be time waste.

'''

# With function


def sub(m, n):
    print('Subtraction :', m - n)


sub(11, 10)

sub(True, False)

sub(10.1, 9.9)

sub(9.9, 8.8)

# sub('ab', 'b')  TypeError: unsupported operand type(s) for -: 'str' and 'str'

sub(10+11j, 9+10j)
