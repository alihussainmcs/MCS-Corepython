import math

integers = ['orange', 6, -8, 'apple']
for i in integers:
    try:
        number_factorial = math.factorial(i)

    except TypeError:
        print("The input is not supported.")
    except ValueError:
        print(i, " is not a positive integer.")

print("---------------------------------------------------")

import sys

number_list = ['a', 2, 2]
for number in number_list:
    try:
        print("The 1st number is", number)
        r = 1 + int(number)
        break
    except:
        print("k", sys.exc_info()[0], "value.")
        print("Next entry.")
print("The addition of", number, "is", r)

print("------------------------------------------------")

try:
    n = 0
    m = 2
    c = m / n
except ZeroDivisionError as e:
    print("The zero can't be divided")
try:
    n = 2
    m = '3'
    p = m + n
except TypeError:
    print('The number is in the string format')


print("-----------------------------------------")
try:
    number = 2
    number = number+'5'
except(TypeError, SyntaxError, ValueError)as e:
    print("The number is given in string format")

