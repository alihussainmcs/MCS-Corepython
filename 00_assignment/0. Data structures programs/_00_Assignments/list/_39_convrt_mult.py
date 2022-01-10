# P39. REQ :  Converting multiple integers into single integer
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


# Python3 program to convert a list
# of integers into a single integer
def convert(list1):
    # Converting integer list to string list
    # and joining the list using join()
    res = int("".join(map(str, list1)))

    return res


list_1 = [1, 2, 3]
print('List :', list_1)
print('Required o/p :', convert(list_1))

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
