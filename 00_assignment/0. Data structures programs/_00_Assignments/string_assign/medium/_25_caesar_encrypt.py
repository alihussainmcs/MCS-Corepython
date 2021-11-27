# P25. REQ :  program to create a Caesar encryption
"""
1. CRUD       -->  Retrieval
2. STATE      -->  string
3. BEHAVIOR   -->  int  |     ==    |   for if-elif
"""

# 0. Mathematics
"""
str_1 = ' i am the python engineer '

o/p   = ' k co vjg ravjqp gpikpggt '
"""

# 1.Builtin functions

print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

str_1 = ' i am the python engineer '
print("String :", str_1)
cipher = ''
shift = 2
for char in str_1:
    if char == ' ':
        cipher = cipher + char
    elif char.isupper():
        cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
        cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

print('Encrypted String :', cipher)
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
