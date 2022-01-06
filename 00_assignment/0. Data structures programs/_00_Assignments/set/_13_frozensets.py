# P13. REQ : Use of frozensets
"""
1. CRUD       -->  Retrieval
2. STATE      -->  frozenset
3. BEHAVIOR   -->  frozenset  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
# use isdisjoint(). Return True if the set has no elements in common with other.
print(x.isdisjoint(y))
# use difference(). Return a new set with elements in the set that are not in the others.
print(x.difference(y))
# new set with elements from both x and y
print(x | y)

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
