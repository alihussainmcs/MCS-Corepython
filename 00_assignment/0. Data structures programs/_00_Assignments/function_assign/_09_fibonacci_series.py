# P09. fibonacci series ?
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =      |   if-elif-else
"""

# 0. Mathematics
"""
The Fibonacci numbers are the numbers in the following integer sequence. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,….
What is the formula for Fibonacci series?
Fibonacci numbers are a sequence of whole numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... This infinite sequence is called
                                                                                            the Fibonacci sequence.
...
What is Fibonacci Sequence?
F0 = 0	F10 = 55
F2 = 1	F12 = 144
F3 = 2	F13 = 233
F4 = 3	F14 = 377
F5 = 5	F15 = 610
"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")


def fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))
# 4 OOPS
print("--------4 Object Oriented        ----------")

# 5 Exception handling
print("--------5 Exception handling     ----------")

# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
