"""
ArithmeticError Exception is the base class for all errors that occur for numeric calculations. It is the base class
for those built-in exceptions like: OverflowError, ZeroDivisionError, FloatingPointError
"""

print("ArithmeticError: 1.ZeroDivisionError   2.OverflowError 3.FloatingPointError")
print("     1.ZeroDivisionError")
# print(7/0)   ZeroDivisionError: division by zero
try:
    7 / 0
except ArithmeticError as e:
    print(e)
print('This is an example_1 of catching ArithmeticError')

print("--------------------------------------------------------")
"""
In Python,FloatingPointError is subclass of ArithmeticError. FloatingPointError occurred with floating point operations 
when floating point exception control (fpectl) is turned on.
To Enable fpectl in Python requires an interpreter compiled with the –with-fpectl flag.

Note : In Python, fpectl module is not built by default, you have explicitly import it to control over the floating 
point units from several hardware manufacturer. This allow the use to turn on the generation of SIGFPE whenever any 
IEEE-754 exceptions Division by Zero, Overflow, or Invalid Operation occurs.
"""
print("     2.OverflowError")

import math
# find the exponential of the specified value
print(math.exp(65))
print(math.exp(-6.89))
# math.exp(750) OverflowError: math range error
# import sy
# import fpectl

try:
    print('FPECTL Control Not Enable:', math.exp(750))
    # fpectl.turnon_sigfpe()
    print('FPECTL Control Enabled:', math.exp(750))
except Exception as err:
    print(err)
    # print(sys.exc_type)
"""
from gw_utility.logging import Logging
def test_floating_point():
    try:
        Logging.log(round(24.601 / 3.5, 4))
    except FloatingPointError as exception:
        # Output expected FloatingPointErrors.
        Logging.log_exception(exception)
    except Exception as exception:
        # Output expected Exceptions.
        Logging.log_exception(exception, False)

"""
