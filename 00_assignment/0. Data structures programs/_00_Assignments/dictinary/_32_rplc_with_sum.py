# P32. REQ : Replace dictionary values with their sum.
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


def sum_math_v_vi(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('V')
        n2 = d.pop('VI')
        d['V+VI'] = n1 + n2
    return list_of_dicts


student_details = [
    {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
    {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
    {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
]
print(sum_math_v_vi(student_details))

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
