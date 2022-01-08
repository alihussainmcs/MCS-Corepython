# P12. REQ : Remove specified index from list and print
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


# Python3 program to remove the index
# element from the list
# using traversal

def remove(list1, pos):
    new_list = []

    # traverse in the list
    for x in range(len(list1)):

        # if index not equal to pos
        if x != pos:
            new_list.append(list1[x])
    print(*new_list)


list_1 = [10, 20, 30, 40, 50]
pos_1 = 2
remove(list_1, pos_1)

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
