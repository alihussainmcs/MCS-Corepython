# P52. print all permutations with given repetition number of given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =   +=    |   for
"""

# 0. Mathematics


# 1.Builtin functions
from xlrd.timemachine import xrange

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")


# 3 Using Functions
print("--------3 Using Functions        ----------")
# Python program to print all permutations with
# duplicates allowed


def toString(list_1):
    return ''.join(list_1)


# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, ln, r):
    if ln == r:
        print(toString(a))
    else:
        for i in xrange(ln, r + 1):
            a[ln], a[i] = a[i], a[ln]
            permute(a, ln + 1, r)
            a[ln], a[i] = a[i], a[ln]  # backtrack


# Driver program to test the above function
string = "abc"
n = len(string)
a_1 = list(string)
permute(a_1, 0, n - 1)

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
