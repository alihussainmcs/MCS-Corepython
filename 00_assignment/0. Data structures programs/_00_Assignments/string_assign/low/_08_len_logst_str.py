# REQ Length of longest string in python


"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |  =   +=    |   if else

"""

# 0. Mathematics
"""
str_1='abcd'
       1234
str_2='uvwxyz'
       123456
       str_2 is longest
1.String initialize
2.Count length of each string
3.Retrieve the longest length string
  
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

"""
1. Initialize the string or get string input from user
2. With builtin function lem(), will found len of each string and Retrieve the lem() value 
3. Compare the length with if else and will get longest string
"""

str_1 = 'abcd'
str_2 = 'uvwxyz'

if len(str_1) > len(str_2):
    print("str_1 is longest ")
elif len(str_1) < len(str_2):
    print("str_2 is longest ")
else:
    print("Both are equal in length")
# 2. Algorithm
print("--------2 Algorithm              ----------")

"""
1. Initialize the string
2. Count the length of the string
3. Use if else to find the longest string 
"""
str_1 = 'abcd'
str_2 = 'uvwxyz'

count_1 = 0
for i in str_1:
    count_1 += 1

count_2 = 0
for i in str_2:
    count_2 += 1

if count_1 > count_2:
    print("str_1 is longest ")
elif count_1 < count_2:
    print("str_2 is longest ")
else:
    print("str_1 and str_2 is of same length ")

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
