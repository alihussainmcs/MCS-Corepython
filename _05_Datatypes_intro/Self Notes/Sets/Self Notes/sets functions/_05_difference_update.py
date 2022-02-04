"""

Python Set difference_update() Method

Example
Remove the items that exist in both sets:

Definition and Usage
The difference_update() method removes the items that exist in both sets.

The difference_update() method is different from the difference() method, because the difference() method
    returns a newset, without the unwanted items, and the difference_update() method removes the unwanted items from
    the original set.

Syntax

set.difference_update(set)

Parameter Values

Parameter	    Description
set	Required.   The set to check for differences in

"""
x = {"apple", "banana", "cherry"}

y = {"google", "microsoft", "apple"}

print('Original set :', x)

print('Original set :', y)

x.difference_update(y)

print('x.difference_update(y)', x)

A = {10, 20, 30, 40, 80}

B = {100, 30, 80, 40, 60}

print('Original set A:', A)

print('Original set B:', B)

# Modifies A and returns None
A.difference_update(B)

# Prints the modified set
print('A.difference_update(B)', A)
