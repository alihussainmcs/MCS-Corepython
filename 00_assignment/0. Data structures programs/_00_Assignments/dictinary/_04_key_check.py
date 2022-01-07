# P04. REQ : Check if a given key already exists in a dictionary.
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

# 3 Using Functions
print("--------3 Using Functions        ----------")
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("Dictionary :", d)


def is_key_present(x):
    if x in d:
        print('Key %i is present in the dictionary' % x)
    else:
        print('Key %i is not present in the dictionary' % x)


is_key_present(5)
is_key_present(9)

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
