# P05. REQ : Get the current memory address and the length in elements of the buffer used to hold an arrays?
# contents and also find the size
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

print("Original array: "+str(array_num))

print("Current memory address and the length in elements of the buffer: ", str(array_num.buffer_info()))

print("The size of the memory buffer in bytes: ", str(array_num.buffer_info()[1] * array_num.itemsize))


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
