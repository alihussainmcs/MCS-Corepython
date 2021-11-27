# P01. REQ : print the index of the character in a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  +=  =    | for
"""

# 0. Mathematics
"""
1. Initialize the string
2. Retrieve the index of chars
str_1 = "abcdxyz"
index=>  0123456     
"""

# 1.Builtin functions
"""
1. Initialize the string or get string input from user
2. With builtin function count(), will found number of repeat of the substring and Retrieve the count() value 
"""
print("--------1 Builtin Functions      ----------")
str_1 = "abcdxyz"
print("String :", str_1)
for i in str_1:
    print("%s" % i, "index is ", str_1.index(i))

# 2. Algorithm

print("--------2 Algorithm              ----------")

j = 0
str_1 = "abcdxyz"
print("String :", str_1)

for i in str_1:
    print(i, "index is ", j)
    j += 1
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
