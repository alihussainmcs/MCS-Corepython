"""
Python Set difference() Method

Example
Return a set that contains the items that only exist in set x, and not in set y:

Definition and Usage

The difference() method returns a set that contains the difference between two sets.

Meaning: The returned set contains items that exist only in the first set, and not in both sets.

Syntax

set.difference(set)

Parameter Values

Parameter	    Description

set	Required. The set to check for differences in

"""

x = {"apple", "banana", "cherry"}

y = {"google", "microsoft", "apple"}

print('Original set :', x)

print('Original set :', y)

z = x.difference(y)

print('x.difference(y) :', z)

A = {'a', 'b', 'c', 'd'}

B = {'c', 'f', 'g'}

print('Original set A:', A)

print('Original set B:', B)

# Equivalent to A-B
print('A.difference(B)', A.difference(B))

# Equivalent to B-A
print('B.difference(A)', B.difference(A))
