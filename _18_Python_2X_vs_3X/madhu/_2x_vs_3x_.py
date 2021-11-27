# important differences in 2x and 3x python

"""
    1.Division operator
    2.print function
    3.Unicode
    4.xrange
    5.Error Handling
    6._future_ module
1. when division operator used 7/5 in 2x results 1, 3x - returns 1.4
2. In 2x we use print 'hello',  In 3x we use print('hello')  otherwise it shown syntactical error
3. in 2x print an implicit type in ASCII, where in 3x implicit type in unicode
   in 2x print(type(b'hello')) returns < type str>
   in 3x print(type(b'hello)) returns < class bytes> bytes and str are differeent
4.in 2x print(
"""

# https://www.geeksforgeeks.org/important-differences-between-python-2-x-and-python-3-x-with-examples/

print("_____Division operator_______")

print(7 / 5)
print(- 7 / 5)

'''
Output in Python 2.x      1    -2
Output in Python 3.x :  1.4   -1.4
'''
print("_____ print function_______")

# print 'Hello, Geeks'	 # Python 3.x doesn't support

print('Hope You like these facts')

'''

Output in Python 2.x :

Hello, Geeks

Hope You like these facts



Output in Python 3.x :

File "a.py", line 1

	print 'Hello, Geeks'

					^

SyntaxError: invalid syntax

'''

print("______unicode________")

# unicode format : strings are stored as unicode
# In Python 2, an implicit str type is ASCII. But in Python 3.x implicit str type is Unicode.
'''

Unicode is the Information Technology standard that is used for encoding, representation, 
and handling of texts in the writing systems.
ASCII (American Standard Code for Information Interchange) represents text in computers 
such as symbols, digits, uppercase letters, and lowercase letters.


Unicode is a universal character encoding standard that assigns a code to every character and 
symbol in every language in the world. Since no other encoding standard supports all languages, 
Unicode is the only encoding standard that ensures that you can retrieve or combine data using 
any combination of languages.


'''

print(type('default string '))

print(type(b'string with b '))

'''

Output in Python 2.x (Bytes is same as str)

<type 'str'>

<type 'str'>


Output in Python 3.x (Bytes and str are different)

<class 'str'>

<class 'bytes'>

'''
# Python 2.x also supports Unicode
print(type('default string '))

print(type(u'string with b '))
'''
Output in Python 2.x (Unicode and str are different)

<type 'str'>

<type 'unicode'>



Output in Python 3.x (Unicode and str are same)

<class 'str'>

<class 'str'>

'''

# 2.x    range --> Iterator  xrange  --> generator
# 3.x    range --> Generator
print("======range===========")
# for x in xrange(1, 5):

# print(x),

for x in range(1, 5):
    print(x)

'''

Output in Python 2.x

1 2 3 4 1 2 3 4



Output in Python 3.x

NameError: name 'xrange' is not defined

'''

print("______ Error Handling_______")
'''
try:
    trying_to_check_error
except NameError, err:
    print err, 'Error Caused' # Would not work in Python 3.x


Output in Python 2.x:

name 'trying_to_check_error' is not defined Error Caused



Output in Python 3.x :

File "a.py", line 3

	except NameError, err:

					^

SyntaxError: invalid syntax

'''

try:
    raise NameError("Name error raised")
except NameError as err:  # NameError,  err
    print(err, 'Error Caused')

print(" __future__ module")

# In below python 2.x code, division works
# same as Python 3.x because we use  __future__

# from __future__ import division

# print 7 / 5     ----> 1.4   returns only 1 without using future module

# print - 7 / 5 --->  -1.4


# from __future__ import print_function

print('GeeksforGeeks')
