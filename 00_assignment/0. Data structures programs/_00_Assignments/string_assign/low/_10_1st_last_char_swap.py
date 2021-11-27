# P01. REQ : First last chars swapping
"""
1. CRUD       -->  Update
2. STATE      -->  string
3. BEHAVIOR   -->  string concatenation  |
"""

# 0. Mathematics
"""
a = 'karnatka'
     01234567
        to
     aarnatkk
     71234560
   
"""
# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
"""
1. Initialize the string
2. separate first and last char from string
3. swap it and retrieve the required string   

"""
print("--------2 Algorithm              ----------")

a = 'karnatka'

print("Given string is : ", a)
b = a[1:-1]
print('Expected string is ', b.join(a[-1]+a[0]))

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
