# P21. REQ : Count the values associated with key in a dictionary
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
student = [{'id': 1, 'success': True, 'name': 'Larry'}, {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
print(sum(d['id'] for d in student))
print(sum(d['success'] for d in student))

print()
# Python3 code to demonstrate working of
# Count keys with particular value in dictionary
# Using sum() + values()

# Initialize dictionary
test_dict = {'Python': 1, 'is': 2, 'best': 3, 'for': 2, 'CS': 2}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize value
K = 2

# Using sum() + values()
# Selective key values in dictionary
res = sum(x == K for x in test_dict.values())

# printing result
print("Frequency of K is : " + str(res))

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
