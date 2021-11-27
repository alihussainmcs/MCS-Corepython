"""
Logical Operators
--------------------

A logical operator is a symbol or word used to connect two or more expressions
In Python, Logical operators are used on conditional statements (either True or False).
They perform Logical AND, Logical OR and Logical NOT operations.

Types:
------
-> Logical AND
-> Logical OR
-> Logical NOT

Logical AND:
------------
Logical  AND operator returns True if both the operands are True else it returns False.

a=10
b=20
if a>0 and b>0:
    print("The numbers are Greater than zero")
else:
    print("The numbers are not greater than zero")

Here the output will be “The numbers are Greater than zero”

Logical OR:
-----------
Logical OR operator returns True if either of the operands is True.
a = 10
b = 12
c = 0

if a or b or c:
    print("At least one number has boolean value as True")
else:
    print("All the numbers have boolean value as False")

Here the output will be “At least one number has boolean value as True”

Logical NOT:
------------
Logical NOT operator work with the single boolean value. If the boolean value is True it returns False and vice-versa.

"""