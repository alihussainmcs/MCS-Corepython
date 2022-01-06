# P03. REQ : Reverse the order of the items in the array.
"""
1. CRUD       -->  Retrieval
2. STATE      -->  array
3. BEHAVIOR   -->  array  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
from array import *

array_num = array('i', [1, 3, 5, 7, 9])
print("Access All items ")

for i in array_num:
    print(i)

array_num.append(10)

array_num.append(101)

print("Access All items after append items in reverse order ")

for i in array_num[::-1]:
    print(i)
print(array_num.reverse())
print(array_num)
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: ", array_num)
array_num.reverse()
print("Reverse the order of the items:")
print(array_num)

# 3 Using Functions
print("--------3 Using Functions        ----------")

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
