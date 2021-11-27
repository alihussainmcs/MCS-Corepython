# P45. REQ :  check if a string contains all letters of the alphabet
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->   str    |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
import string
alphabet = set(string.ascii_lowercase)
str_1 = 'The quick brown fox jumps over the lazy dog'
print(set(str_1.lower()) >= alphabet)
str_2 = 'The quick brown fox jumps over the lazy cat'
print(set(str_2.lower()) >= alphabet)

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
