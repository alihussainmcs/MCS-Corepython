"""
 10. copy()
      list.copy(obj)   make copy of the list
"""
list1 = [1, 2, 3, 4, 5]
print("Before copy list1 : ", list1)
list2 = list1.copy()
print("After copy list2  : ", list2)
print("Normal copy function : ", id(list1), id(list2))
list1.append(100)

print("After append : list1 :", list1)
print("After append : list2 :", list2)

# 2nd way of copy

list1 = [1, 2, 3, 4, 5]
list2 = list1
print("Variable  copy : ", id(list1), id(list2))
list1.append(100)
print("After var copy :", list1, list2)
list2.extend(([11, 22]))
print("After var copy :", list1, list2)

"""
difference between shallow and deep copying:

A shallow copy means constructing a new collection object and then populating it with references to the child objects 
found in the original. In essence, a shallow copy is only one level deep. The copying process does not recurse and 
therefore won’t create copies of the child objects themselves.

A deep copy makes the copying process recursive. It means first constructing a new collection object and then 
recursively populating it with copies of the child objects found in the original. Copying an object this way walks 
the whole object tree to create a fully independent clone of the original object and all of its children.
"""

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy

print("Original List :", xs)

print("shallow copy List :", ys)

xs.append(['new sublist'])

print("Original List after adding a value in xs.append(['new sublist']):", xs)

print("shallow copy List :", ys)

xs[1][0] = 'X'

print("Original List after adding a value in xs[1][0] = 'X'):", xs)

print("shallow copy List :", ys)



import copy
ab = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ba = copy.deepcopy(ab)
print("Original List :", ab)

print("deepcopy List :", ba)
ab[1][0] = 'X'

print("Original List after adding value ab[1][0] ='X':", ab)

print("deepcopy List :", ba)
