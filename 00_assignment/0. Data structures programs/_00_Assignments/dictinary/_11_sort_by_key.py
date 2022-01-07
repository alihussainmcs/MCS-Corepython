# P11. REQ : Sort a dictionary by key
"""
1. CRUD       -->  Update
2. STATE      -->  Dictionary
3. BEHAVIOR   -->  dict  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ', d)
print('Sorted dictionary by keys :')
for key in sorted(d):
    print(key, d[key])

print('                 Second way                    ')
a = {1: 2, 2: 1, 4: 3, 3: 4, 6: 5, 5: 6}
print('Original dictionary : ', a)

# this will print a sorted list of the keys
print(sorted(a.keys()))
# this will print the sorted list with items.
print(sorted(a.items()))
# 3 Using Functions
print("--------3 Using Functions        ----------")

# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

di = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(OrderedDict(sorted(di.items())))

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
