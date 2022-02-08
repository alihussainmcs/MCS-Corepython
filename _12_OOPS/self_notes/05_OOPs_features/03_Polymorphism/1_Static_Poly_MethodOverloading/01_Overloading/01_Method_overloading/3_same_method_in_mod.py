"""
# In JAVA

def product(a, b):
    res = a * b
    print(res)
def product(a, b, c):
    res = a * b * c
    print(res)
product(10,20)  # 7th line
product(10,20,30) # 10th line
"""


# First product method.
# Takes two argument and print their
# product
"""
def product(a):
    pass
"""


def product(a, b):
    res = a * b
    print(res)

# product(10) TypeError: product() missing 1 required positional argument: 'b'

# We can call only in one way,by passing both arguments


product(3, 4)  # Positional args
product(a=3, b=4)  # Keyword args
product(b=4, a=3)  # Keyword args

print("Function product : ", product)
# Second product method
# Takes three argument and print their
# product


def product(a, b, c=1):
    p = a * b * c
    print(p)


print("Function product : ", product)
# Uncommenting the below line shows an error
product(4, 5)
# This line will call the second product method
product(3, 4)
product(4, 5, 5)


def sum(a, b, c=0):
    return a + b + c


print("Sum :", sum(10, 20))

print("Sum :", sum(10, 20, 30))


def sub_1(a, b):
    return a-b


"""
def sub_1(a, b, c):
    return a-b-c

# sub_1(20, 30) TypeError: sub_1() missing 1 required positional argument: 'c'
"""
""" 
def sub_1(a, b, c, d):
    return a-b-c-d

# sub_1(30,20,10) TypeError: sub_1() missing 1 required positional argument: 'd'
"""

print('Subtraction is :', sub_1(20, 10))

print("..........................................................")


class Human:

    def sayHello(self, name=None):

        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


# Create instance
obj = Human()

# Call the method
obj.sayHello()

# Call the method with a parameter
obj.sayHello('Guido')
