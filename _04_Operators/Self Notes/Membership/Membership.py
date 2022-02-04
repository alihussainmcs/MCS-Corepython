"""
Membership Operator:
--------------------
Membership operators are used to test if a sequence is presented in an object.

--> in
--> not in

in:
--
Returns True if a sequence with the specified value is present in the object.

not in:
-------
Returns True if a sequence with the specified value is not present in the object.

Example:
--------

x = ["bat", "ball"]

print("bat" in x)

--> Returns True because a sequence with the value Bat is in the List.

x = ["bat", "ball"]

print("ground" not in x)

--> Returns True because a sequence with the value ground is not in the List.

"""

a = ['1', 1, True]

b = [False, 0, '']

c = [True, '1', 1, False, 0, '']

print('a :', a)

print('b :', b)

print('c :', c)
