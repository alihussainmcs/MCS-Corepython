# P17. REQ : Find the highest 3 values in a dictionary.
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
# Python program to demonstrate
# finding 3 highest values in a Dictionary

from collections import Counter

# Initial Dictionary
my_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69}

k = Counter(my_dict)

# Finding 3 highest values
high = k.most_common(3)

print("Initial Dictionary:")
print(my_dict, "\n")


print("Dictionary with 3 highest values:")
print("Keys: Values")

for i in high:
	print(i[0]," :",i[1]," ")

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
