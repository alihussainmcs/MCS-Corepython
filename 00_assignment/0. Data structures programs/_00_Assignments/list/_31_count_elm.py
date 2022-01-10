# P31. REQ : Counting number elements within a specified ranges
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

# 3 Using Functions
print("--------3 Using Functions        ----------")


def count_range_in_list(li, min1, max1):
    ctr = 0
    for x in li:
        if min1 <= x <= max1:
            ctr += 1
    return ctr


list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(list2, 'a', 'e'))

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
