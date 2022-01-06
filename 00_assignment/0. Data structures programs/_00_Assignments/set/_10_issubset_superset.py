# P10. REQ : Issubset and issuperset.
"""
1. CRUD       -->  Retrieval
2. STATE      -->  Set
3. BEHAVIOR   -->  Set  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
"""
Python set issubset() method returns True if all elements of a set A are present in another set B which is passed as an
 argument and returns false if all elements not present.
 
Python set issuperset() method returns True if all elements of a set A occupies set B which is passed as an argument and 
returns false if all elements of B are not present in A. This means if A is a superset of B then it returns true; 
else False
"""
# create a set

# Python program to demonstrate working of
# issubset().
print("                     issubset()                      ")
A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print("Set A :", A)

print("Set B :", B)
# Returns True
print('A.issubset(B) :', A.issubset(B))

# Returns False
# B is not subset of A
print('B.issubset(A) :', B.issubset(A))

# Python program to demonstrate working of
# issuperset().
print("                     issuperset()                      ")

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
print("Set A :", A)

print("Set B :", B)
print("A.issuperset(B) : ", A.issuperset(B))

# B is superset of A
print("B.issuperset(A) : ", B.issuperset(A))
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
