# P30. REQ : Get unique values
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")
# Python3 code to demonstrate
# list frequency of elements
# using Counter() + set() + list comprehension
from collections import Counter

# initializing list
test_list = [[3, 5, 4],
             [6, 2, 4],
             [1, 3, 6]]

# printing original list
print("The original list : " + str(test_list))

# using Counter() + set() + list comprehension
# list frequency of elements
res = dict(Counter(i for sub in test_list for i in set(sub)))

# printing result
print("The list frequency of elements is : " + str(res))

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
