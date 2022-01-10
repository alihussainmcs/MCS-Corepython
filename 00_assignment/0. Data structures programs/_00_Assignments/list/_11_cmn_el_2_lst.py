# P11. REQ :  Find common element from 2 lists
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |
"""

# 0. Mathematics

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")


# Python program to find the common elements
# in two lists
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if a_set & b_set:
        print(a_set & b_set)
    else:
        print("No common elements")


a_1 = [1, 2, 3, 4, 5]
b_1 = [5, 6, 7, 8, 9]
common_member(a_1, b_1)

a_2 = [1, 2, 3, 4, 5]
b_2 = [6, 7, 8, 9]
common_member(a_2, b_2)

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
