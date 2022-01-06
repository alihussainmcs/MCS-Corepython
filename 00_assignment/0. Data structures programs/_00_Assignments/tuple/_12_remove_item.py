# P12. REQ :  remove an item from a tuple
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
tpl = 2, 4, 5, 6, 2, 3, 4, 4, 7
print('Given Tuple :', tpl)

# tuples are immutable, so you can not remove elements
# using merge of tuples with the + operator you can remove an item and it will create a new tuple
tpl = tpl[:2] + tpl[3:]
print('Tuple after merge or remove [2] index item :', tpl)
# converting the tuple to list
lst = list(tpl)
# use different ways to remove an item of the list
lst.remove(6)
# converting the tuple to list
tpl = tuple(lst)
print('tuple to list and then remove 6 item and converted to tuple :', tpl)

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
