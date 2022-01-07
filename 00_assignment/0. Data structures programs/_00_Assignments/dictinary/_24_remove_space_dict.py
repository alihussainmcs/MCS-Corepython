# P24. REQ : Remove spaces from dictionary keys.
"""
1. CRUD       -->  Update
2. STATE      -->  Dictionary
3. BEHAVIOR   -->  dict  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")

student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ", student_list)
student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
print("New dictionary: ", student_dict)

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
