"""
Introduction
The map(), filter() and reduce() functions bring a bit of functional programming to Python. All three of these are
convenience functions that can be replaced with List Comprehensions or loops, but provide a more elegant and short-hand
approach to some problems.

Before continuing, we'll go over a few things you should be familiar with before reading about the
aforementioned methods:

What is an anonymous function/method or lambda?

An anonymous method is a method without a name, i.e. not bound to an identifier like when we define a method
 using def method:.

Note: Though most people use the terms "anonymous function" and "lambda function" interchangeably - they're not the
same. This mistake happens because in most programming languages lambdas are anonymous and all anonymous functions
are lambdas. This is also the case in Python. Thus, we won't go into this distinction further in this article.

What is the syntax of a lambda function (or lambda operator)?
lambda arguments: expression
Think of lambdas as one-line methods without a name. They work practically the same as any other method in Python,
for example:
"""

print(".................lambda...............")


def add_1(x, y):
    return x + y


# Can be translated to:

z = lambda x, y: x + y
print('z(10, 11) :', z(10, 11))
"""
Lambdas differ from normal Python methods because they can have only one expression, can't contain any statements and 
their return type is a function object. So the line of code above doesn't exactly return the value x + y but the 
function that calculates x + y.
Why are lambdas relevant to map(), filter() and reduce()?

All three of these methods expect a function object as the first argument. This function object can be a pre-defined 
method with a name (like def add(x,y)).

Though, more often than not, functions passed to map(), filter(), and reduce() are the ones you'd use only once, so 
there's often no point in defining a referencable function.

To avoid defining a new function for your different map()/filter()/reduce() needs - a more elegant solution would be 
to use a short, disposable, anonymous function that you will only use once and never again - a lambda.

The map() Function
The map() function iterates through all items in the given iterable and executes the function we passed as an argument
 on each of them.

The syntax is:

map(function, iterable(s))
We can pass as many iterable objects as we want after passing the function we want to use:
"""

# Without using lambdas
print("......................map...........................")


def starts_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]


map_object = map(starts_with_A, fruit)

print(list(map_object))

print("............2nd example map..............")


# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# Double all numbers using map and lambda

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# Add two lists using map and lambda
print("............3rd example map..............")

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
print("............4th example map..............")

# List of strings
lst = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, lst))
print(test)

# List of strings
lst = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, lst))
print(test)

"""
This code will result in:

[True, False, False, True, False]
As we can see, we ended up with a new list where the function starts_with_A() was evaluated for each of the elements
 in the list fruit. The results of this function were added to the list sequentially.

A prettier way to do this exact same thing is by using lambdas:
"""
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(list(map_object))

"""
We get the same output:

[True, False, False, True, False]
Note: You may have noticed that we've cast map_object to a list to print each element's value. We did this because 
calling print() on a list will print the actual values of the elements. Calling print() on map_object would print 
the memory addresses of the values instead.

The map() function returns the map_object type, which is an iterable and we could have printed the results like 
this as well:
"""

for value in map_object:
    print(value)

# If you'd like the map() function to return a list instead, you can just cast it when calling the function:

result_list = list(map(lambda s: s[0] == "A", fruit))

"""
The filter() Function

Similar to map(), filter() takes a function object and an iterable and creates a new list.

As the name suggests, filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the
 function we passed returns True.

The syntax is:

filter(function, iterable(s))
Using the previous example, we can see that the new list will only contain elements for which the starts_with_A() 
function returns True:
"""

# Without using lambdas
print("......................filter...........................")


def starts_with_A(s):
    return s[0] == "A"


fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

print(list(filter_object))

"""
Running this code will result in a shorter list:

['Apple', 'Apricot']
Or, rewritten using a lambda:
"""

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))

print("..........2nd example......................")

# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

print("..............3rd example........................")
# random list
random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)

# converting to list
filtered_list = list(filtered_iterator)

print(filtered_list)

"""
The reduce() Function

reduce() works differently than map() and filter(). It does not return a new list based on the function and iterable
 we've passed. Instead, it returns a single value.

Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.

The syntax is:

reduce(function, sequence[, initial])
reduce() works by calling the function we passed for the first two items in the sequence. The result returned by the 
function is used in another call to function alongside with the next (third in this case), element.

This process repeats until we've gone through all the elements in the sequence.

The optional argument initial is used, when present, at the beginning of this "loop" with the first element in the 
first call to function. In a way, the initial element is the 0th element, before the first one, when provided.

reduce() is a bit harder to understand than map() and filter(), so let's look at a step by step example:

We start with a list [2, 4, 7, 3] and pass the add(x, y) function to reduce() alongside this list, without an initial 
value

reduce() calls add(2, 4), and add() returns 6

reduce() calls add(6, 7) (result of the previous call to add() and the next element in the list as parameters), and 
add() returns 13

reduce() calls add(13, 3), and add() returns 16

Since no more elements are left in the sequence, reduce() returns 16

The only difference, if we had given an initial value would have been an additional step - 1.5. where reduce() would 
call add(initial, 2) and use that return value in step 2.

"""
print("......................reduce...........................")

from functools import reduce


def add(x, y):
    return x + y


lst = [2, 4, 7, 3]
print(reduce(add, lst))

"""
Running this code would yield:

16
Again, this could be written using lambdas:
"""

from functools import reduce

lst = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, lst))
print("With an initial value: " + str(reduce(lambda x, y: x + y, lst, 10)))

"""
And the code would result in:

16
With an initial value: 26
"""

print(".............3rd example...........")

# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

print(".........4th ex..................")
# Returns the sum of all the elements using `reduce`
result = reduce((lambda a, b: a + b), [1, 2, 3, 4])
print(result)
