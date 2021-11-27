# P59. REQ :   find the maximum occurring character in a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |
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


def get_max_char(str1):
    a = 256
    ctr = [0] * a
    m = -1
    ch = ''
    for i in str1:
        ctr[ord(i)] += 1

    for i in str1:
        if m < ctr[ord(i)]:
            m = ctr[ord(i)]
            ch = i
    return ch


print(get_max_char("Python: Get file creation and modification date/times"))
print(get_max_char("abdicate"))

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
