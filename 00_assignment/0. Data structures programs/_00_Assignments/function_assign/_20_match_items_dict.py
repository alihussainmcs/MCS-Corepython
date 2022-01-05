# P20. REQ : function to match the item in two dictionaries.
"""
1. CRUD       -->  Retrieval
2. STATE      -->  Dictionary
3. BEHAVIOR   -->  dict  |     =    |   for   if-else
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
aa = {'a': 1, 'c': 3, 'b': 2}
bb = {'a': 1, 'b': 2, 'd': 4}

c = [k for k, v in aa.items() if k in bb]

print(c)
# 3 Using Functions
print("--------3 Using Functions        ----------")


def match_item_dict(a, b):
    print([k for k, v in a.items() if k in b])


match_item_dict(aa, bb)
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
