# P11. REQ : Insert a new item before the second element in an existing array.
"""
1. CRUD       -->  Update
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

num_list = [1, 2, 6, -8]

array_num = array('i', [])

print("Items in the list: " + str(num_list))

print("Append items from the list: ")

array_num.fromlist(num_list)

print("Items in the array: "+str(array_num))

array_num.insert(1, 8)

print("Items in the array: "+str(array_num))


array_num.pop(3) 
print("Items in the array after pop 3 index : "+str(array_num))

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
