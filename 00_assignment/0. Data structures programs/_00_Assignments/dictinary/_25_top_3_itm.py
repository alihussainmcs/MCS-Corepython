# P25. REQ : Get the top three items in a shop.
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

from heapq import nlargest
from operator import itemgetter

items = {'Milk': 45.50, 'Sugar': 35, 'Coffee': 41.30, 'Egg': 55, 'Tea': 24}
print("Dictionary items :", items)
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)


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
