# Add() -----> Method used to add one item to a set.

# update() -----> Method used to add two or more items to the set.

"""
We can add a single element using the add() method, and multiple elements using the update() method.
The update() method can take tuples, lists, strings or other sets as its argument.
"""

# add
a = {"apple", "banana", "cherry"}

print("The original set:", a)

a.add("orange")

print("The set after adding the item:", a)  # updated set

# add

# add multiple elements
b = {9, 6, 10, 34}

print("The original Set:", b)

b.add(2)

print("The set after adding the item:", b)  # updated set

# adding list and set
c = {5, 11, 12, 13, 14}

print("The original Set:", c)

c.add(4)

print("The set after adding the item:", c)  # updated set

c.add(5)

print("The set after adding the item:", c)  # updated set

c.add(101)

print("The set after adding the item:", c)  # updated set

c.add(True)

print("The set after adding the item:", c)  # updated set

c.add(False)

print("The set after adding the item:", c)  # updated set
