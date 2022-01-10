# P32. REQ : Check a list contains sublist
"""
1. CRUD       -->  Retrieval
2. STATE      -->  list
3. BEHAVIOR   -->  list  |     =    |
"""

# 0. Mathematics
"""

"""

# 1.Builtin functions
print("--------1 Builtin Functions      ----------")

# 2. Algorithm
print("--------2 Algorithm              ----------")
# to check if list is subset of other
# using all()

# initializing list
test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5, 4]

# printing original lists
print("Original list : " + str(test_list))
print("Original sub list : " + str(sub_list))

# using all() to
# check subset of list
flag = 0
if all(x in test_list for x in sub_list):
	flag = 1

# printing result
if flag:
	print("Yes, list is subset of other.")
else:
	print("No, list is not subset of other.")

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
