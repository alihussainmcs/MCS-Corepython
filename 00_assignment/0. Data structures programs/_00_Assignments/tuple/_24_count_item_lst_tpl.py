# P24. REQ :  count the elements in a list until an element is a tuple
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
# create a tuple
num = [10, 20, 30, (10, 20), 40]
ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)

# 3 Using Functions
print("--------3 Using Functions        ----------")


# Python program to count the items
# until a list is encountered
def Count(li):
    counter = 0
    for num in li:
        if isinstance(num, tuple):
            break
        counter = counter + 1
    return counter


# Driver Code
li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
print(Count(li))

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
