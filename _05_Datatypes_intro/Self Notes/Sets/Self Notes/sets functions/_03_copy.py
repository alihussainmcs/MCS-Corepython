"""
Python Set copy() Method

Example
Copy the fruits set:

Definition and Usage
The copy() method copies the set.

Syntax

set.copy()

Parameter Values

No parameters


"""

fruits = {"apple", "banana", "cherry"}

print('Original set :', fruits)

x = fruits.copy()

print('Copy   set :', x)

print(id(fruits))

print(id(x))

set1 = {1, 2, 3, 4}

print('Original set :', set1)

# function to copy the set
set2 = set1.copy()

# prints the copied set
print('Copy   set :', set2)

print(id(set1))

print(id(set2))

set1 = {True, 2, False, 4.2}

print('Original set :', set1)

# function to copy the set
set2 = set1.copy()

# prints the copied set
print('Copy   set :', set2)

print(id(set1))

print(id(set2))
