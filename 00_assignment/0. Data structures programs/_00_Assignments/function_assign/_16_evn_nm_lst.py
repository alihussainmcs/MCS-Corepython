# P16. REQ :  print the even numbers from a given list
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
list_1 = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7]
print('Given list :', list_1)
lst_2 = []
for i in list_1:
    if i % 2 == 0:
        lst_2.append(i)

print('Even numbers from given list :', lst_2)
# 3 Using Functions
print("--------3 Using Functions        ----------")


def even_num_lst(lst_1):
    print('Given list :', lst_1)
    lst_3 = []
    for j in lst_1:
        if j % 2 == 0:
            lst_3.append(j)

    print('Even numbers from given list :', lst_3)


even_num_lst([2, 3, 4, 5, 6, 7, 8])

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
