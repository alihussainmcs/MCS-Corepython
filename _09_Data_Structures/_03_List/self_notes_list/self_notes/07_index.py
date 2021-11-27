"""
 7. index
      list.index(obj)    Returns the lowest index in list that obj appears
"""

list1 = [23, 76, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]
print("Given list1 is :", list1)

print("List index(23) : ", list1.index(23))

print("List index(53) : ", list1.index(53))

print("List index(25) : ", list1.index(25))

print("List index(7) : ", list1.index(7))

print("List index(49) : ", list1.index(59))

# print("List index(-1) : ", list1.index(-1))
# output:  ValueError: -1 is not in list
