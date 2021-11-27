# REQ : Upper lower case of a string

"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int   | = | +=
"""

# 0. Mathematics
"""
str_1 = 'AdsFretaSrtfsArN'
         lower:dsreartfsr   Uper: AFSAN                  
"""
# 1.Builtin functions

print("--------1 Builtin Functions      ----------")
# 2. Algorithm
"""
1. Initialize the string
2. take two empty string for lower and upper char store
3. use for loop and separate and add lower and upper char in variables 
4. retrieve the required output

"""
print("--------2 Algorithm              ----------")
str_1 = 'AdsFretaSrtfsArN'
print("String : ", str_1)
v = ''
u = ''
for i in str_1:
    if i.islower():
        v += i
    elif i.upper():
        u += i

print('Lower words string : ', v)
print('Upper words string : ', u)

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
