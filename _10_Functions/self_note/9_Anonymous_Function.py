# 1 mark : Find square of given value 5
print("Square of value : ", 5*5)

print('Square of number : ', 25*25)

# 2 mark : Find square of given value 15
val = 15
print("Square of value : ", val*val)

num = 10  # Find square of given number 10
print('Square of number : ', num*num)

# 3 marks : Find square of given value 25
val = 25


def find_square(in_no):
    result = in_no * in_no
    return result


sq_val = find_square(val)
print("Square of value : ", sq_val)

# REQ : Find cube of a given number 5

ab = 5


def cube(n):
    print('Cube of the number :', n**3)


cube(ab)

# Use lambda functions  ==> map filter reduce
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
print(".................Lambda Function..................")

sum = lambda a, b: a + b
print("Lambda  : Summation of value : ", sum(10, 20))

sub = lambda a, b: a - b
print("Lambda  : Subtraction of value : ", sub(10, 20))

sq_val = lambda num1: num1 * num1
print("Lambda  : Square of value : ", sq_val(5))

qub_val = lambda v: v**3
print("Lambda  : Qube of value : ", qub_val(5))


# Covert to function


def sq_val(num1):
    return num1*num1


print("Function : Square of value : ", sq_val(5))


# Function memory allocation
x = 10

print("x value, address : ", x, ',', id(x))


def get_data():
    print("Welcome to my method")
    return "Hello World"


res = get_data()   # Function calling
print("Result is : ", res)

print("Function body address ", get_data)  # Get function body address
print("Function address ", id(get_data))  # Get function address

print("................Anonymous/ Lambda Function .....................")

print("Syntax:   lambda arguments : expression ")

x = lambda a: a + 10
print(" x = lambda a: a + 10 ")
print('x(5) is :', x(5))


x = lambda a, b: a * b
print(" x = lambda a, b : a * b ")
print('x(5, 6) is :', x(5, 6))

x = lambda a, b, c: a + b + c
print(" x = lambda a, b, c: a + b + c ")
print('x(5, 6, 2) is :', x(5, 6, 2))

x = lambda a, b: a - b
print('Subtraction using lambda function ...')
print(x(2, 1))

print(x)  # <function <lambda> at 0x000001B0152F2A60> function body address
print(id(x))  # 1855781284448
