"""
Python Array

Note: When people say arrays in Python, more often than not, they are talking about Python lists. If that's the case,

here, we will focus on a module named array. The array module allows us to store a collection of numeric values.

Creating Python Arrays
To create an array of numeric values, we need to import the array module. For example:

"""

import array as arr

a = arr.array('d', [1.1, 3.5, 4.5])
print(a)

"""
Here, we created an array of float type. The letter d is a type code. This determines the type of the array 
during creation.

Commonly used type codes are listed as follows:

Code	    C Type	        Python Type	    Min bytes
b	        signed          char int	        1
B	        unsigned        char int	        1
u	        Py_UNICODE	    Unicode	            2
h	        signed          short int	        2
H	        unsigned        short	int	        2
i	        signed int	    int	                2
I	        unsigned int	int	                2
l	        signed long	    int	                4
L	        unsigned long	int	                4
f	        float	        float	            4
d	        double	        float	            8

We will not discuss different C types in this article. We will use two type codes in this entire article: i for 
integers and d for floats.

Note: The u type code for Unicode characters is deprecated since version 3.3. Avoid using as much as possible.

Accessing Python Array Elements
We use indices to access elements of an array:

"""
print()

import array as arr

a = arr.array('i', [2, 4, 6, 8])

print("First element:", a[0])
print("Second element:", a[1])
print("Last element:", a[-1])

"""
Note: The index starts from 0 (not 1) similar to lists.

Slicing Python Arrays
We can access a range of items in an array by using the slicing operator :.

"""

print()

import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5])  # 3rd to 5th
print(numbers_array[:-5])  # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])  # beginning to end


print()

import array as arr

numbers = arr.array('i', [1, 2, 3, 5, 7, 10])

# changing first element
numbers[0] = 0
print(numbers)     # Output: array('i', [0, 2, 3, 5, 7, 10])

# changing 3rd to 5th element
numbers[2:5] = arr.array('i', [4, 6, 8])
print(numbers)     # Output: array('i', [0, 2, 4, 6, 8, 10])

print()

import array as arr

numbers = arr.array('i', [1, 2, 3])

numbers.append(4)
print(numbers)     # Output: array('i', [1, 2, 3, 4])

# extend() appends iterable to the end of the array
numbers.extend([5, 6, 7])
print(numbers)     # Output: array('i', [1, 2, 3, 4, 5, 6, 7])

print()


import array as arr

odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])

numbers = arr.array('i')   # creating empty array of integer

print(numbers)

print()


import array as arr

number = arr.array('i', [1, 2, 3, 3, 4])

del number[2]  # removing third element
print(number)  # Output: array('i', [1, 2, 3, 4])

del number  # deleting entire array

print()

import array as arr

numbers = arr.array('i', [10, 11, 12, 12, 13])

numbers.remove(12)
print(numbers)   # Output: array('i', [10, 11, 12, 13])

print(numbers.pop(2))   # Output: 12
print(numbers)   # Output: array('i', [10, 11, 13])


"""
When to use arrays?
Lists are much more flexible than arrays. They can store elements of different data types including strings. And, if 
you need to do mathematical computation on arrays and matrices, you are much better off using something like NumPy.

So, what are the uses of arrays created from the Python array module?

The array.array type is just a thin wrapper on C arrays which provides space-efficient storage of basic C-style 
data types. If you need to allocate an array that you know will not change, then arrays can be faster and use less 
memory than lists.

Unless you don't really need arrays (array module may be needed to interface with C code), the use of the array module 
is not recommended.

"""