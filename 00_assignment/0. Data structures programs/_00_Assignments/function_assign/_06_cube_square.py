# P06. find cube/square of a number

"""
1. CRUD       -->  Retrieve
2. STATE      -->  integer
3. BEHAVIOR   -->  int  |     |  =
"""

# 0. Mathematics
"""
num = 5

cube --> 5**3 = 125
square --> 5**2 = 25
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

num = 5

print("Given number     :", num)
print("Square of number :", num ** 2)
print("Cube   of number :", num ** 3)

# 3 Using Functions
print("--------3 Using Functions        ----------")


def square_cube(num_1):
    print("Given number     :", num_1)
    print("Square of number :", num_1 ** 2)
    print("Cube   of number :", num_1 ** 3)


square_cube(6)
# 4 OOPS
print("--------4 Object Oriented        ----------")


class SquareCube:
    def __init__(self, num_2):
        self.num_2 = num_2

    def square_cube_method(self):
        print("Given number     :", self.num_2)
        print("Square of number :", self.num_2 ** 2)
        print("Cube   of number :", self.num_2 ** 3)


sq = SquareCube(7)
sq.square_cube_method()
# 5 Exception handling
print("--------5 Exception handling     ----------")


try:
    def square_cube(num_1):
        print("Given number     :", num_1)
        print("Square of number :", num_1 ** 2)
        print("Cube   of number :", num_1 ** 3)


    square_cube('a')
except TypeError as te:
    print("Exception part ! ", te)


# 6 File Handling
print("--------6 File Handling          ----------")

# 7 Database interaction MVC
print("--------7 Database interaction   ----------")

# 8 UI Interaction
print("--------8 UI Interaction         ----------")
