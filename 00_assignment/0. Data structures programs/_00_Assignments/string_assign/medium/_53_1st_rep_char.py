# P51. REQ :  find the first repeated character in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |   for, if
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


def first_repeated_char(str1):
    for index, c in enumerate(str1):
        if str1[:index + 1].count(c) > 1:
            return c
    return "None"


print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcd"))

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
