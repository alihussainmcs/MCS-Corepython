"""
Tuple:
------
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets.
tuples are ordered, it means that the items have a defined order, and that order will not change.
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Creating a Tuple:
-----------------
x = ("apple", "banana", "cherry")
print(x)

Changing Tuple Values:
----------------------
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list,
and convert the list back into a tuple.

Example:
---------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)-------------------------->("apple", "kiwi", "cherry")

Tuple Methods:
--------------
-->count()	Returns the number of times a specified value occurs in a tuple.
-->index()	Searches the tuple for a specified value and returns the position of where it was found."""


# Tuple Packing:

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple

# Packing a tuple:

fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(fruits)
print(a)
print(b)
print(c)

# Tuple Unpacking:

# we are also allowed to extract the values back into variables. This is called "unpacking"

a = (1, 2, 3)

i, j, k = a
print("The Values Are")
print(i)
print(j)
print(k)
