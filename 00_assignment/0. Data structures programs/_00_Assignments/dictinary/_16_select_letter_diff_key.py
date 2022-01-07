# P16. REQ : Create and display all combinations of letters, selecting each letter from a different key in a dictionary
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
import itertools

d = {'1': ['a', 'b'], '2': ['c', 'd']}
print("The original dict is : " + str(d))

for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

# Python3 code to demonstrate working of
# Dictionary key combinations
# Using list comprehension + enumerate()

# Initializing dict
test_dict = {'python': 1, 'is': 2, 'the': 3, 'best': 4}

# printing original dict
print("The original dict is : " + str(test_dict))

# Dictionary key combinations
# Using list comprehension + enumerate()
test_dict = list(test_dict)
res = [(x, y) for idx, x in enumerate(test_dict) for y in test_dict[idx + 1:]]

# printing result
print("The dictionary key pair list is : " + str(res))

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
