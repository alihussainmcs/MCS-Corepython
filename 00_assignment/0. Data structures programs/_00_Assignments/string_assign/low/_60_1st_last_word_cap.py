# P60. REQ : capitalize first and last letters of each word of a given string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  str  |  +=  =    | for
"""

# 0. Mathematics
"""
str_1 = ' i am hungry '
                ||
                --
expected o/p = ' I AM HungrY'      

"""
# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1 = 'i am hungry man'
print("String :", str_1)

str_1 = str_1.title()
str_2 = ''
print("String :", str_1)
for i in str_1.split():
    str_2 += i[:-1] + i[-1].upper() + ' '

print('Expected result :', str_2)

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
