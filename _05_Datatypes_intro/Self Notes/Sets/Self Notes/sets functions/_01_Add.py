# Add() -----> Method used to add one item to a set.

# update() -----> Method used to add two or more items to the set.

'''
We can add a single element using the add() method, and multiple elements using the update() method.
The update() method can take tuples, lists, strings or other sets as its argument.
'''

# add
a = {"apple", "banana", "cherry"}
print("The original set:", a)

a.add("orange")

print("The set after adding the item:", a)   # updated set


# update

# add multiple elements
b = {9, 6, 10, 34}
print("The original Set:", b)
b.update([2, 3, 4])
print("The Updated Set:", b)

# adding list and set
c = {5, 11, 12, 13, 14}
print("The original Set:", c)
c.update([4, 5], {1, 6, 8})
print("The updated set:", c)