"""
Assertion Error
Assertion is a programming concept used while writing a code where the user declares a condition to be true using
assert statement prior to running the module. If the condition is True, the control simply moves to the next line of
code. In case if it is False the program stops running and returns AssertionError Exception.

The function of assert statement is the same irrespective of the language in which it is implemented, it is a
language-independent concept, only the syntax varies with the programming language.
Syntax of assertion:
assert condition, error_message(optional)
Example 1: Assertion error with error_message.

# AssertionError with error_message.
x = 1
y = 0
assert y != 0, "Invalid Operation"  # denominator can't be 0    # AssertionError: Invalid Operation
print(x / y)

o/p:

Traceback (most recent call last):
  File "<input>", line 3, in <module>
AssertionError: Invalid Operation

"""

# Handling it manually
try:
    x = 1
    y = 0
    assert y != 0, "Invalid Operation"
    print(x / y)

# the error_message provided by the user gets printed
except AssertionError as msg:
    print(msg)

print("---------------------------------------------------------------------------")
import math


def assertion_error(a, b, c):
    try:
        assert a != 0, "Not a quadratic equation as coefficient of x ^ 2 can't be 0"
        d = (b * b - 4 * a * c)
        assert d >= 0, "Roots are imaginary"
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        print("Roots of the quadratic equation are :", r1, "", r2)
    except AssertionError as ms:
        print(ms)


assertion_error(-1, 5, -6)
assertion_error(1, 1, 6)
assertion_error(2, 12, 18)
assertion_error(0, 12, 18)
