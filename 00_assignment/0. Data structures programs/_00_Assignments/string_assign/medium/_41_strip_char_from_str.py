# P41. REQ :  strip a set of characters from a string
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  str  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

str_2 = "The quick brown fox jumps over the lazy dog."
print("String :", str_2)
st = 'aeiou'
s = ''
for i in str_2:
    if i not in st:
        s += i

print('Exp O/P : ', s)
# 3 Using Functions
print("--------3 Using Functions        ----------")


def strip_chars(str_1, chars):
    return "".join(i for i in str_1 if i not in chars)


print("\nOriginal String: ")
print("The quick brown fox jumps over the lazy dog.")
print("After stripping a,e,i,o,u")
print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
print()

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
