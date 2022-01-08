# P08. REQ :  Check list is empty or not
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
lst = [10, 1, 5, 3, 1, 11, 19, 10, 11]
lst_1 = []
print('Given List 1:', lst)
print('Type: ', type(lst))
print('Checking list empty :', lst is None)

print('Given List 2:', lst_1)

print('Type: ', type(lst_1))

print('Checking list empty :', lst_1 is not None)

# 3 Using Functions
print("--------3 Using Functions        ----------")


# Python code to check for empty list
# Explicit way
def Enquiry(lis1):
    if len(lis1) == 0:
        return 0
    else:
        return 1


lis2 = []
if Enquiry(lis2):
    print("The list is not empty")
else:
    print("Empty List")

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
