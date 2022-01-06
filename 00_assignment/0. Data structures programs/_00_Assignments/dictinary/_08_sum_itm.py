# P08. REQ : Sum all the items in a dictionary
"""
1. CRUD       -->  Update
2. STATE      -->  Dictionary
3. BEHAVIOR   -->  dict  |     =    |
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


# all items in a Dictionary

# Function to print sum
def returnSum(my_dict):
    list_1 = []
    for i in my_dict:
        list_1.append(my_dict[i])
    final = sum(list_1)

    return final


# Driver Function
dict_1 = {'a': 100, 'b': 200, 'c': 300}
print('Dictionary :', dict_1)
print("Sum :", returnSum(dict_1))

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
