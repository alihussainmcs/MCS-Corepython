# Discard---> Used to remove an item.

"""

remove() method can also be used to remove the item.
The only difference is if the item to remove does not exist, remove() will raise an error
whereas discard() method will not raise the error

Definition and Usage
The discard() method removes the specified item from the set.

This method is different from the remove() method, because the remove() method will raise an error if the specified
    item does not exist, and the discard() method will not.

Syntax
set.discard(value)

Parameter Values

Parameter	Description
value	Required. The item to search for, and remove
"""

b = {9, 6, 10, 34}

# printing the set before deleting

print("The original Set:", b)

b.discard(34)

# printing the set after deleting

print("The updated set:", b)

numbers = {2, 3, 4, 5}

numbers.discard(3)

print('numbers = ', numbers)

numbers.discard(10)

print('numbers = ', numbers)

numbers = {2, 3, 5, 4}

# Returns None
# Meaning, absence of a return value
print(numbers.discard(3))

print('numbers =', numbers)
