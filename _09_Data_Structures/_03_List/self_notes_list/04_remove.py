"""
 4. remove
      list.remove(obj)    Removes object obj from list
"""

list1 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print("Before removal : ", list1)
list1.remove(34)
print("After removal  : ", list1)

list1 = [23, 14, 12, 46, 34, 14, 7, 2, 14, 19, 25]
print("Before removal : ", list1)
#  list1.remove(14)
list1.pop(5)
print("After removal  : ", list1)
