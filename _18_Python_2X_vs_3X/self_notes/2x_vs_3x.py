from __future__ import division

# https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html

"""
Difference Between Python 2 and 3 :

The two major versions of Python that were introduced to the world were Python 2 and Python 3.
Although they are both just different versions of the same programming language, surprisingly,
there are striking differences between the two and it would be extremely exciting to take a look at the differences
between Python 2 and Python 3. In the past, there has been a lot of debate around the fact that which one of the two
versions is better to use.

What is Python 2?
Python 2.0 was introduced to the tech world in the year 2000. Created by the BeOpen Python Labs
team, the purpose of the introduction of Python 2 was to make programming simple and easy to learn for the common mass.

Python 2 was successful in implementing the technical details of the Python Enhancement Proposal (PEP). However,
after the introduction of Python 3, Python 2 could not find a lot of its usage in the tech world and the year 2020
marked the end of Python 2’s legacy with Python 2.7 being its latest version. Given below is a timeline of the
release of the various versions of the Python 2.X series:

Python 2.0 – October 16, 2000
Python 2.1 – April 17, 2001
Python 2.2 – December 21, 2001
Python 2.3 – July 29, 2003
Python 2.4 – November 30, 2004
Python 2.5 – September 19, 2006
Python 2.6 – October 1, 2008
Python 2.7-July 3, 2010

What is Python 3?

Released in the year 2008, Python 3 was not just another version of Python 2 after debugging. The introduction of Python
was mostly surrounded with the motive that redundancy – writing repetitive code or writing the same piece of code again
and again – should be removed from coding. Python 3 is backward incompatible and aims at eliminating the problems which
new programmers face while learning a programming language.

Given below is a timeline of the release of the various versions of the Python 3.X series:

Python 3.0 – December 3, 2008
Python 3.1 – June 27, 2009
Python 3.2 – February 20, 2011
Python 3.3 – September 29, 2012
Python 3.4-March 16, 2014
Python 3.5 – September 13, 2015
Python 3.6- October 2016
Python 3.7- June 2018.


Sections :
The __future__ module
The print function
    Python 2
    Python 3
Integer division
    Python 2
    Python 3
Unicode
    Python 2
    Python 3
xrange
    Python 2
    Python 3
The __contains__ method for range objects in Python 3
Note about the speed differences in Python 2 and 3
Raising exceptions
    Python 2
    Python 3
Handling exceptions
    Python 2
    Python 3
The next() function and .next() method
    Python 2
    Python 3
For-loop variables and the global namespace leak
    Python 2
    Python 3
Comparing unorderable types
    Python 2
    Python 3
Parsing user inputs via input()
    Python 2
    Python 3
Returning iterable objects instead of lists
    Python 2
    Python 3
Banker’s Rounding
    Python 2
    Python 3

"""

'''
The __future__ module
Python 3.x introduced some Python 2-incompatible keywords and features that can be imported via the in-built __future__ 
module in Python 2. It is recommended to use __future__ imports it if you are planning Python 3.x support for your code.
 For example_1, if we want Python 3.x’s integer division behavior in Python 2, we can import it via

from __future__ import division
'''

from platform import python_version

'''
The print function
Very trivial, and the change in the print-syntax is probably the most widely known change, but still it is worth 
mentioning: Python 2’s print statement has been replaced by the print() function, meaning that we have to wrap the 
object that we want to print in parentheses.

Python 2 does’t have a problem with additional parentheses, but in contrast, Python 3 would raise a SyntaxError if we 
called the print function the Python 2-way without the parentheses.

Python 2

print 'Python', python_version()
print 'Hello, World!'
print('Hello, World!')
print "text", ; print 'print more text on the same line'


output :
Python 2.7.6
Hello, World!
Hello, World!
text print more text on the same line
'''

# Python 3
print('Python', python_version())
print('Hello, World!')

print("some text,", end="")
print(' print more text on the same line')

'''
o/p :
Python 3.6.5
Hello, World!
some text, print more text on the same line
'''

# print 'Hello, World!'  SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hello, World!')?

'''
Integer division
This change is particularly dangerous if you are porting code, or if you are executing Python 3 code in Python 2, since 
the change in integer-division behavior can often go unnoticed (it does’t raise a SyntaxError).
So, I still tend to use a float(3)/2 or 3/2.0 instead of a 3/2 in my Python 3 scripts to save the Python 2 guys some 
trouble (and vice versa, I recommend a from __future__ import division in your Python 2 scripts).

Python 2
print 'Python', python_version()
print '3 / 2 =', 3 / 2
print '3 // 2 =', 3 // 2
print '3 / 2.0 =', 3 / 2.0
print '3 // 2.0 =', 3 // 2.0

o/p :
Python 2.7.6
3 / 2 = 1
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
'''
print("-------------------------------------------------------------------------------------")
# Python 3
print('3 / 2 =', 3 / 2)
print('3 // 2 =', 3 // 2)
print('3 / 2.0 =', 3 / 2.0)
print('3 // 2.0 =', 3 // 2.0)

'''
o/p : 
3 / 2 = 1.5
3 // 2 = 1
3 / 2.0 = 1.5
3 // 2.0 = 1.0
'''

'''
Unicode
Python 2 has ASCII str() types, separate unicode(), but no byte type.

Now, in Python 3, we finally have Unicode (utf-8) strings, and 2 byte classes: byte and bytearrays.

Python 2

print type(unicode('this is like a python3 str type'))

o/p :
<type 'unicode'>

print type(b'byte type does not exist')

o/p :
<type 'str'>
'''
print("-------------------------------------------------------------------------------------")

# Python 3
print('strings are now utf-8 \u03BCnico\u0394é!')

# o/p :strings are now utf-8 μnicoΔé!


'''xrange 
The usage of xrange() is very popular in Python 2.x for creating an iterable object, e.g., in a for-loop or 
list/set-dictionary-comprehension. The behavior was quite similar to a generator (i.e., “lazy evaluation”), 
but here the xrange-iterable is not exhaustible - meaning, you could iterate over it infinitely. 

Thanks to its “lazy-evaluation”, the advantage of the regular range() is that xrange() is generally faster if you 
have to iterate over it only once (e.g., in a for-loop). However, in contrast to 1-time iterations, it is not 
recommended if you repeat the iteration multiple times, since the generation happens every time from scratch! 

In Python 3, the range() was implemented like the xrange() function so that a dedicated xrange() function does not 
exist anymore (xrange() raises a NameError in Python 3). 

import timeit

n = 10000
def test_range(n):
    return for i in range(n):
        pass

def test_xrange(n):
    for i in xrange(n):
        pass  
        
        

Python 2

print 'Python', python_version()

print '\ntiming range()'
%timeit test_range(n)

print '\n\ntiming xrange()'
%timeit test_xrange(n)

o/p: 

Python 2.7.6

timing range()
1000 loops, best of 3: 433 µs per loop


timing xrange()
1000 loops, best of 3: 350 µs per loop

        

The __contains__ method for range objects in Python 3 
Another thing worth mentioning is that range got a “new” 
__contains__ method in Python 3.x (thanks to Yuchen Ying, who pointed this out). The __contains__ method can speedup 
“look-ups” in Python 3.x range significantly for integer and Boolean types. 


Note about the speed differences in Python 2 and 3 Some people pointed out the speed difference between Python 3’s 
range() and Python2’s xrange(). Since they are implemented the same way one would expect the same speed. However the 
difference here just comes from the fact that Python 3 generally tends to run slower than Python 2. 

Raising exceptions Where Python 2 accepts both notations, the ‘old’ and the ‘new’ syntax, Python 3 chokes (and raises 
a SyntaxError in turn) if we don’t enclose the exception argument in parentheses: 

Python 2
'''

# raise IOError, "file error"  SyntaxError: invalid syntax

'''
Handling exceptions
Also the handling of exceptions has slightly changed in Python 3. In Python 3 we have to use the “as” keyword now

Python 2
print 'Python', python_version()
try:
    let_us_cause_a_NameError
except NameError, err:
    print err, '--> our error message'
    
o/p :
    
Python 2.7.6
name 'let_us_cause_a_NameError' is not defined --> our error message
'''
print("-------------------------------------------------------------------------------------")

# Python 3

print('Python', python_version())
try:
    let_us_cause_a_NameError
except NameError as err:
    print(err, '--> our error message')


'''
The next() function and .next() method
Since next() (.next()) is such a commonly used function (method), this is another syntax change (or rather change in 
implementation) that is worth mentioning: where you can use both the function and method syntax in Python 2.7.5, the 
next() function is all that remains in Python 3 (calling the .next() method raises an AttributeError).

Python 2
print 'Python', python_version()

my_generator = (letter for letter in 'abcdefg')

next(my_generator)
my_generator.next()
Python 2.7.6





'b'
'''
print("-------------------------------------------------------------------------------------")

# Python 3
print('Python', python_version())

my_generator = (letter for letter in 'abcdefg')

next(my_generator)

# my_generator.next()  AttributeError: 'generator' object has no attribute 'next'

'''
For-loop variables and the global namespace leak
Good news is: In Python 3.x for-loop variables don’t leak into the global namespace anymore!

This goes back to a change that was made in Python 3.x and is described in What’s New In Python 3.0 as follows:

“List comprehensions no longer support the syntactic form [... for var in item1, item2, ...]. Use [... for var in (
item1, item2, ...)] instead. Also note that list comprehensions have different semantics: they are closer to 
syntactic sugar for a generator expression inside a list() constructor, and in particular the loop control variables 
are no longer leaked into the surrounding scope.” 

Python 2
print 'Python', python_version()

i = 1
print 'before: i =', i

print 'comprehension: ', [i for i in range(5)]

print 'after: i =', i

o/p : 
Python 2.7.6
before: i = 1
comprehension:  [0, 1, 2, 3, 4]
after: i = 4

'''
print("-------------------------------------------------------------------------------------")

# Python 3
print('Python', python_version())

i = 1
print('before: i =', i)

print('comprehension:', [i for i in range(5)])

print('after: i =', i)


'''
Comparing unorderable types
Another nice change in Python 3 is that a TypeError is raised as warning if we try to compare unorderable types.

Python 2
print 'Python', python_version()
print "[1, 2] > 'foo' = ", [1, 2] > 'foo'
print "(1, 2) > 'foo' = ", (1, 2) > 'foo'
print "[1, 2] > (1, 2) = ", [1, 2] > (1, 2)

o/p :
Python 2.7.6
[1, 2] > 'foo' =  False
(1, 2) > 'foo' =  True
[1, 2] > (1, 2) =  False




# Python 3
print('Python', python_version())
print("[1, 2] > 'foo' = ", [1, 2] > 'foo')
print("(1, 2) > 'foo' = ", (1, 2) > 'foo')
print("[1, 2] > (1, 2) = ", [1, 2] > (1, 2))
TypeError: '>' not supported between instances of 'list' and 'str'

Parsing user inputs via input() Fortunately, the input() function was fixed in Python 3 so that it always stores the 
user inputs as str objects. In order to avoid the dangerous behavior in Python 2 to read in other types than strings, 
we have to use raw_input() instead. 

Python 2

Python 2.7.6
[GCC 4.0.1 (Apple Inc. build 5493)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> my_input = input('enter a number: ')

enter a number: 123

>>> type(my_input)
<type 'int'>

>>> my_input = raw_input('enter a number: ')

enter a number: 123

>>> type(my_input)
<type 'str'>


Python 3
Python 3.4.1
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> my_input = input('enter a number: ')

enter a number: 123

>>> type(my_input)
<class 'str'>

Returning iterable objects instead of lists As we have already seen in the xrange section, some functions and methods 
return iterable objects in Python 3 now - instead of lists in Python 2. 

Since we usually iterate over those only once anyway, I think this change makes a lot of sense to save memory. 
However, it is also possible - in contrast to generators - to iterate over those multiple times if needed, 
it is only not so efficient. 

And for those cases where we really need the list-objects, we can simply convert the iterable object into a list via 
the list() function. 

Python 2
print 'Python', python_version()

print range(3)
print type(range(3))
Python 2.7.6
[0, 1, 2]
<type 'list'>

'''
print("-------------------------------------------------------------------------------------")

# Python 3
print('Python', python_version())

print(range(3))
print(type(range(3)))
print(list(range(3)))

'''
Some more commonly used functions and methods that don’t return lists anymore in Python 3:

zip()

map()

filter()

dictionary’s .keys() method

dictionary’s .values() method

dictionary’s .items() method

Banker’s Rounding Python 3 adopted the now standard way of rounding decimals when it results in a tie (.5) at the 
last significant digits. Now, in Python 3, decimals are rounded to the nearest even number. Although it’s an 
inconvenience for code portability, it’s supposedly a better way of rounding compared to rounding up as it avoids the 
bias towards large numbers. For more information, see the excellent Wikipedia articles and paragraphs: 

https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
https://en.wikipedia.org/wiki/IEEE_floating_point#Roundings_to_nearest
Python 2
print 'Python', python_version()
Python 2.7.12
round(15.5)
16.0
round(16.5)
17.0
Python 3
print('Python', python_version())
Python 3.5.1
round(15.5)
16
round(16.5)
16
'''
