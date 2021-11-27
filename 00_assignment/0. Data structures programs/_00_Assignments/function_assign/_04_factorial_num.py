# P04. factorial of given number

"""
1. CRUD       -->  Update
2. STATE      -->  integer
3. BEHAVIOR   -->  int  |   for  |  ==
"""

# 0. Mathematics
"""
num = 5

factorial --->  5x4x3x2x1 = 120
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print('Factorial of %i is' % num, fact)

# 3 Using Functions
print("--------3 Using Functions        ----------")


def fact_func(num_1):
    fact_1 = 1
    for j in range(1, num_1 + 1):
        fact_1 *= j
    print('Factorial of %i is' % num_1, fact_1)


fact_func(6)

# 4 OOPS
print("--------4 Object Oriented        ----------")


class FactClass:
    def __init__(self, num_2):
        self.num_2 = num_2

    def fact_method(self):
        fact_1 = 1
        for j in range(1, self.num_2 + 1):
            fact_1 *= j
        print('Factorial of %i is' % self.num_2, fact_1)


cla_ob = FactClass(7)
cla_ob.fact_method()

# 5 Exception handling
print("--------5 Exception handling     ----------")

try:
    def fact_func(num_1):
        fact_1 = 1
        for j in range(1, num_1 + 1):
            fact_1 *= j
        print('Factorial of %i is' % num_1, fact_1)


    fact_func('a')
except TypeError as te:
    print(te)


print("-------------------------------------------------------------------")

try:
    def fact_func(num_1):
        fact_1 = 1
        for j in range(1, num_1 + 1):
            fact_1 *= j
        print('Factorial of %i is' % num_1, fact_1)


    fact_func(8)
except TypeError as te:
    print(te)


# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
