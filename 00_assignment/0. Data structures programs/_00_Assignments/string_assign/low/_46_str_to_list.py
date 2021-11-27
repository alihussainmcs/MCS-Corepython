# P46. REQ : convert a string in a list
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  +=  =    | for
"""

# 0. Mathematics

"""
str_1 = "abcdxyz"

list_1 = ['a','b','c','d','x','y','z']
"""
# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2. With builtin function list(), convert str in list 
"""
print("--------1 Builtin Functions      ----------")
str_1 = "abcdxyz"
print("String :", str_1)
print("String to List ", list(str_1))

# 2. Algorithm

print("--------2 Algorithm              ----------")

str_1 = "abcdxyz"
print("String :", str_1)
list_1 = []
for i in str_1:
    list_1.append(i)
print("String to List ", list_1)

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
