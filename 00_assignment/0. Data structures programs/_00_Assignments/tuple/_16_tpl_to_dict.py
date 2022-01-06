# P16. REQ : convert a tuple to a dictionary
"""
1. CRUD       -->  Retrieval
2. STATE      -->  String
3. BEHAVIOR   -->  tuple  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
# create a tuple

tpl = (("Hulk", 93), ("Wonder Woman", 45), ("Thor", 65), ("Batman", 88), ("Superman", 70), ("Super Girl", 52))
print('Given tuple :', tpl)
dict_1 = dict()

for student, score in tpl:
    dict_1.setdefault(student, []).append(score)
print('tuple to dictionary :', dict_1)

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
