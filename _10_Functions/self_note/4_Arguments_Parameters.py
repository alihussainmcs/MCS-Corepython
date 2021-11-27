# REQ : Find sum of 2 given numbers

# 1. STATE
"""
num1 = int(input("Enter number1 :"))
num2 = int(input("Enter number2 :"))
"""
a = True
b = False


# 2. Behaviour


def sum_1(x, y):
    result = x + y
    print("Summation is :", result)


sum_1(a, b)
sum_1(101, 201)
sum_1(True, 201)
sum_1(True, 10.6)
sum_1(True, 10 + 0j)
sum_1(10, 10 + 111j)
sum_1('a', 'b')
sum_1('ali', 'hussain')
sum_1([1, 2], [3, 4])
sum_1([1, 2, 3, 4], [1, 2, 3, 4, 5])
sum_1((1, 2, 3, 7, 8, 9), (11, 22, 33, 77, 88, 99))
# sum_1({1, 2}, {3, 4})  TypeError: unsupported operand type(s) for +: 'set' and 'set'
# sum_1({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'}) TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# sum_1({1: 101, 2: 102}, {3: 103, 4: 104}) TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

"""
8, 9 lines     : a, b       ==> Variables 
               : 101,201    ==> values
15             : x, y       ==> Parameters
20,21,22...... :            ==> arguments     

"""

"""
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that are sent to the function when it is called.

"""
