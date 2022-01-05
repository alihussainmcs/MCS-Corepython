# P05. REQ : add an item in a tuple.
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
tpl = (4, 6, 2, 8, 3, 1)
print('Given tuple :', tpl)
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tpl = tpl + (9,)
print('Tuple after merge an item :', tpl)
# adding items in a specific index
tpl = tpl[:5] + (15, 20, 25) + tpl[:5]
print('adding an item on a specific index :', tpl)
# converting the tuple to list
lst = list(tpl)
# use different ways to add items in list
lst.append(30)
tpl = tuple(lst)
print('in list added item and convert in tuple :', tpl)

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
