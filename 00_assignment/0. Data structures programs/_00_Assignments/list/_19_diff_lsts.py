# P19. REQ : Difference between 2 lists
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


# Python code t get difference of two lists
# Using set()
def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


li_1 = [10, 15, 20, 25, 30, 35, 40]
li_2 = [25, 30, 40, 35]
print('List 1 :', li_1)
print('List 2 :', li_2)

print('Difference of list1 and list2 :', Diff(li_1, li_2))

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
