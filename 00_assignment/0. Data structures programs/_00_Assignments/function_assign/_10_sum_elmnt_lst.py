# P10. sum all the numbers in a list
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =      |   for
"""

# 0. Mathematics
"""
list_1 = [2, 4, 6]
sum = 12
"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
list_1 = [2, 4, 6]
print('Given list :', list_1)
print('Sum of list elements :', sum(list_1))
# 2. Algorithm

print("--------2 Algorithm              ----------")
list_2 = [4, 6]
print('Given list :', list_2)
sum_1 = 0
for i in list_2:
    sum_1 += i
print('Sum of list elements :', sum_1)
# 3 Using Functions
print("--------3 Using Functions        ----------")


def sum_elements(list_3):
    print('Given list :', list_3)
    print('Sum of list elements :', sum(list_3))


sum_elements([10, 20, 30])
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
