# P48. REQ : swap comma and dot in a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    | for
"""

# 0. Mathematics
"""
str_1 = '32.567,89'
            ^^
            ||
str_1 = '32,567.89'

1. Initialize the string
2. Replace comma and dot 

"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
str_1 = '32.567,89'
print("String :", str_1)

maketrans = str_1.maketrans
amount = str_1.translate(maketrans(',.', '.,'))
print('String after replace :', amount)

# 2. Algorithm

print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")

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
