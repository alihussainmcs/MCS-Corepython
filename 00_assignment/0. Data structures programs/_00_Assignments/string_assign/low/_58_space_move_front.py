# P58. REQ : move spaces to the front of a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    | for
"""

# 0. Mathematics
"""
str_1 = ' i am h un gry ! '
                ||
                --
expected o/p = '       iamhungry'      

"""
# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1 = ' i am h un gry ! '
print("String with space :", str_1)
count = 0
for i in str_1:
    if i == ' ':
        count += 1
str_2 = ' '*5 + str_1.replace(' ', '')
print("String with space move on front :", str_2)

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
