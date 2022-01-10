# P17. REQ : First,Last elements whose square value is between 1 and 30,except first 5
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
lst = []
for i in range(1, 11):
    lst.append(i ** 2)

print('List : ', lst)

req = []
for i in lst:
    if i <= 30:
        req.append(i)

print('Square number between 1-30 :', req)
print('1st square number between 1-30:', req[0])
print('last square number between 1-30:', req[-1])

print('First,Last elements whose square value is between 1 and 30,except first 5 : ', None)
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
