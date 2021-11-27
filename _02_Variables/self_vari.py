"""
What is a Variable in Python?
A Python variable is a reserved memory location to store values. In other words, a
variable in a python program gives data to the computer for processing.
Every value in Python has a datatype. Different data types in Python are Numbers,
List, Tuple, Strings, Dictionary, etc. Variables can be declared by any name or even
alphabets like a, aa, abc, etc
Variable Naming Rules in Python
1. Variable name should start with letter(a-zA-Z) or underscore (_).
Valid : age , _age , Age
Invalid : 1age
2.In variable name, no special characters allowed other than underscore (_).
Valid : age_ , _age
Invalid : age_*
3.Variables are case sensitive.
age and Age are different, since variable names are case sensitive.
4.Variable name can have numbers but not at the beginning.
Example: Age1
5.Variable name should not be a Python keyword.Keywords are also called as reserved
words.
Example
pass, break, continue.. etc are reserved for special meaning in Python. So, we should
not declare keyword as a variable name.
How to Declare and use a Variable
Let see an example. We will declare variable "a" and print it.
a=100
print (a)
Re-declare a Variable
You can re-declare the variable even after you have declared it once.
a=100
print(a)
a=’AECS Jaduguda’
print(a)
Concatenate Variables
a='AECS'
b=1
print(a+b)
will throw error , as we cannot concatenate two different datatype. But
a='AECS'
b=1
print(a+str(b))
will display
AECS1
Delete a variable
You can also delete variable using the command del "variable name".
The below table displays the list of available assignment operators in Python
language.
ASSIGNMENT OPERATORS
= x = 25 Value 25 is assigned to x
+= x += 25 This is same as x = x + 25
-= x -= 25 Same as x = x – 25
*= x *= 25 This is same as x = x * 25
/= x /= 25 Same as x = x / 25
%= x %= 25 This is identical to x = x % 25
//= x //= 25 Same as x = x // 25
**= x **= 25 This is same as x = x ** 25
>>= x >>= 25 Same as x = x >> 25
L-value and R-Value
An lvalue (locator value) represents an object that occupies some identifiable
location in memory (i.e. has an address). rvalues are defined by exclusion. Every
expression is either an lvalue or an rvalue, so, an rvalue is an expression that does not
represent an object occupying some identifiable location in memory.
(a) A left value or l-value is an assignable object. It is any expression that may occur on
the left side of an assignment. Variables are obvious l-values, but so are items in lists.
(b) A right value or r-value is any expression that has a value that may appear on the
right of an assignment. In python, everything is an r-value.
(c) Traditionally, the underscore ( ) is used as a place-holder for an l-value when we
don't care about the result of the assignment.
(d) In assignment, a tuple of l-values is, itself an l-value:
(a,b,c) = (1,2,3)
a,b,c = 1,2,3
(a,b),_,c = (1,2,),9,3
Each of these effectively assigns a=1, b=2, and c=3.
(e) These complex assignments happen in parallel, so we can exchange values with:
a,b = b,a
Really: it's tuple assignment!
(f) Here's Euler's algorithm for finding greatest common divisors:
def gcd(a,b):
while a > 0:
a,b = (b,a) if a > b else (b%a,a)
return b
(g) when an asterisk precedes a variable name used as an l-value, it means assign this
variable the remaining r-values as a list. This is very powerful:
car,*cdr = (1,2,3)
cdr
[2, 3]
Summary
 Variables are referred to "envelop" or "buckets" where information can be
maintained and referenced. Like any other programming language Python also
uses a variable to store the information.
 Variables can be declared by any name or even alphabets like a, aa, abc, etc.
 Variables can be re-declared even after you have declared them for once
 In Python you cannot concatenate string with number directly, you need to
declare them as a separate variable, and after that, you can concatenate number
with string
 Declare local variable when you want to use it for current function
 Declare Global variable when you want to use the same variable for rest of the
program
 To delete a variable, it uses keyword "del".

"""

print("this is variable ")
