"""
 3. insert(index, obj): Inserts object obj into list at offset index
"""

list1 = [1, 2, 3, 4, 5]

print("Before index : ", list1)

list1[0] = 150  # [150, 2, 3, 4, 5]  Replace the value in index

print("After index   : ", list1)

list1.insert(0, 100)  # [100, 150, 2, 3, 4, 5] Insert the value in index

print("After insert  : ", list1)

list1.insert(5, [10, 20])

print("After insert   : ", list1)
