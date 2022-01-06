# P17. REQ :  unzip a list of tuples into individual lists.
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  tuple  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

# Unzip a list of tuples
# using zip() and * operator

# initializing list of tuples
test_list = [('Thor', 1), ('Hulk', 2), ('Wonder Woman', 3), ('Super Girl', 4)]

# Printing original list
print("Original list is : " + str(test_list))

# using zip() and * operator to
# perform Unzipping
res = list(zip(*test_list))

# Printing modified list
print("Modified list is : " + str(res))
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
