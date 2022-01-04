# P11. multiply all the numbers in a list
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =  +=     |   for
"""

# 0. Mathematics
"""
list_1 = [2, 4, 6]
multi = 48
"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")
list_2 = [4, 6]
print('Given list :', list_2)
multi_1 = 1
for i in list_2:
    multi_1 *= i
print('multiplication of list elements :', multi_1)
# 3 Using Functions
print("--------3 Using Functions        ----------")


def multi(list_1):
    print('Given list :', list_1)
    multi_2 = 1
    for j in list_1:
        multi_2 *= j
    print('multiplication of list elements :', multi_2)


multi([2, 4, 5, 10])

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
