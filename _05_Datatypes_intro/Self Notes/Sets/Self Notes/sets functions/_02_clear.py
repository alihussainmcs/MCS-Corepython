"""

Python Set clear() Method

Remove all elements from the fruits set:

Definition and Usage

The clear() method removes all elements in a set.

Syntax

set.clear()

Parameter Values
No parameters

"""

fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

# set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

print('Vowels (before clear):', vowels)

# clearing vowels
vowels.clear()

print('Vowels (after clear):', vowels)

# set of number
g = {6, 0, 4, 1}

print('set before clear:', g)

# clearing numbers
g.clear()

print('set after clear:', g)

# set of number
g1 = {True, False, 10.01, 10, 10+8j}

print('set before clear:', g1)

# clearing numbers
g1.clear()

print('set after clear:', g1)
