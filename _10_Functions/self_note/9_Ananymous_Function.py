# 1 mark : Find square of given value 5
print("Square of value : ", 5*5)


# 2 mark : Find square of given value 15
val = 15
print("Square of value : ", val*val)


# 3 marks : Find square of given value 25
val = 25


def find_square(in_no):
    result = in_no * in_no
    return result


sq_val = find_square(val)
print("Square of value : ", sq_val)


# Use lambda functions  ==> map filter reduce
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
print(".................Lambda Function..................")
sq_val = lambda num: num * num
print("Lambda  : Square of value : ", sq_val(5))

qub_val = lambda v: v**3
print("Lambda  : Qube of value : ", qub_val(5))


# Covert to function


def sq_val(num):
    return num*num


print("Function : Square of value : ", sq_val(5))


# Function memory allocation
x = 10
print("x value, address : ", x, ',', id(x))


def get_data():
    print("Welocome to my method")
    return "Hello World"


res = get_data()   # Function calling
print("Result is : ", res)

print("Function body address ", get_data)  # Get function body address
print("Function address ", id(get_data))  # Get function body address

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

