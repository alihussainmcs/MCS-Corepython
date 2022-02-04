"""
Identity Operators:
----------------------
Identity operators are used to compare the objects,not if they are equal, but if they are actually the same object,
with the same memory location


is---------------------------->Returns True if both variables are the same object

is not------------------------->Returns True if both variables are not the same object

Example:
--------
a=10
b=20
print(a is b)

Here the output will be False because both are different


a=10
b=10
print(a is b)

Here the output will be True because both are same

"""

a = 10

b = 10

c = 20

print('a :', a)

print('b :', b)

print('c :', c)

print('a is b :', a is b)

print('a is c :', a is c)

print('a is not b :', a is not b)

print('a is not c :', a is not c)
