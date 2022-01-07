# P14. REQ : Combine two dictionary adding values for common keys.
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
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)
print(d)

# Python program to combine two dictionary
# adding values for common keys
# initializing two dictionaries
dict1 = {'a': 12, 'b': 25, 'c': 9}
dict2 = {'d': 100, 'e': 200, 'b': 300}

# adding the values with common key
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass

print(dict2)

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
