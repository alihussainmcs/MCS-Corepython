# P27. REQ : Finding a second smallest number
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

# Python program to find smallest and second smallest elements
import math


def print2Smallest(arr):
    arr_size = len(arr)
    if arr_size < 2:
        print("Invalid Input")
        return

    first = second = math.inf
    for i in range(0, arr_size):

        # If current element is smaller than first then
        # update both first and second
        if arr[i] < first:
            second = first
            first = arr[i]

        # If arr[i] is in between first and second then
        # update second
        elif arr[i] < second and arr[i] != first:
            second = arr[i]

    if second == math.inf:
        print("No second smallest element")
    else:
        print('The smallest element is', first, 'and',
              ' second smallest element is', second)


arr1 = [12, 13, 1, 10, 34, 1]
print('List : ', arr1)
print2Smallest(arr1)

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
