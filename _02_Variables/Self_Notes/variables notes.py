"""
What is a Variable in Python?
A Python variable is a reserved memory location to store values.
In other words, a variable in a python program gives data to the computer for processing.
Every value in Python has a datatype.

Different data types in Python:
-------------------------------
1. Numbers
2. List
3. Tuple
4. Strings
5. Dictionary

Variables can be declared by any name or even alphabets like a, aa, abc, etc.

Variable Naming Rules in Python:
--------------------------------
1. Variable name should start with letter(a-z A-Z) or underscore (_).
Valid : age , _age , Age
 Invalid : 1age

2. In variable name, no special characters allowed other than underscore (_).
Valid : age_ , _age
Invalid : age_*

3. Variables are case sensitive.
age and Age are different, since variable names are case sensitive.

4. Variable name can have numbers but not at the beginning.
Example: Age1

5. Variable name should not be a Python keyword. Keywords are also called as reserved words.
Example: pass, break, continue.. etc are reserved for special meaning in Python.
So, we should not declare keyword as a variable name.

How to Declare and use a Variable:
----------------------------------
Let see an example_1. We will declare variable "a" and print it.
a=100
print (a)

Re-declare a Variable:
----------------------
You can re-declare the variable even after you have declared it once.
a=100
print (a)
a=’world’
print(a)---------------->world

Concatenate Variables:
----------------------
a='world'
b=1
print (a+b)----------------->will throw error
As we cannot concatenate two different datatype.

But
a='world'
b=1
print (a+str(b))-------------->will display world1

You can get the data type of a variable with the type() function.
For ex:
x = 5
y = "John"
print(type(x))-------------------><class ‘int’>
print(type(y))-------------------><class ‘str’>

String variables can be declared either by using single or double quotes:
For ex:
x = "John"
"""
