# P19. REQ :   function to check whether a string is a pangrams or not
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |   for   if-else
"""

# 0. Mathematics
"""
Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
str_1 ='Pack my box with five dozen liquor jugs'
"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

# 3 Using Functions
print("--------3 Using Functions        ----------")
# Check if the string is pangrams


def pangrams(str_2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str_2.lower():
            return False

    return True


str_1 = 'the quick brown fox jumps over the lazy dog'

# str_1 = 'function to check whether a string is a pangrams or not'
print('Given string :', str_1)
if pangrams(str_1):
    print("Given string is pangrams string ")
else:
    print("Given string is not pangrams string")

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
