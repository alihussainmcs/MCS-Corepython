import array as ar

print("...........................Arrays...............................")

"""

ARRAYS:
-------------------------------------------------------------------------------
 - Are used to store multiple values in single variable 
 - An array is a collection of items stored at contiguous memory locations.

"""

# arr_1 = ar.array('a',[1, 2, 3, 4, 5, 6, 7]) ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
arr_1 = ar.array('i', [1, 2, 3, 4, 5, 6, 7])

print("Type of arr_1 is ", type(arr_1))

print('Array arr_1 is ', arr_1)

print("..............Iteration with array................")

for i in arr_1:
    print('Element of array arr_1 is ', i)

arr_2 = ar.ArrayType('i', (1, 2, 3, 5, 6, 9, 11, 22))

print('Array arr_2 is : ', arr_2)

arr_4 = ar.ArrayType('i', {101: '1', 102: '2', 103: 90898767})
print('Array arr_4 is : ', arr_4)

# arr_5 = ar.array('I', [1, True, 10.5, 'Python', 10+20j]) #  TypeError: array item must be integer
# print('Array arr_5 is : ', arr_5)

# arr_5 = ar.array('I', ['1', 'True', '10.5', 'Python', '10+20j'])  # TypeError: an integer is required (got type str)
# print('Array arr_5 is : ', arr_5)

dict_1 = {101: 1, 102: 2}
arr_5 = ar.ArrayType('i', dict_1)
print('Array arr_5 is : ', arr_5)

# dict_2 = {'1': 1, '2': 2}
# arr_6 = ar.ArrayType('i', dict_2)
# print('Array arr_5 is : ', arr_6)  # TypeError: an integer is required (got type str)

# Adding elements to array
print("..............Adding elements in array ............................")

arr_3 = ar.ArrayType('i', {1, 3, 4, 5, 99, 101})
print('Array arr_3 is : ', arr_3)

arr_3.insert(1, 102)
arr_3.insert(1, 102)

print('Array arr_3 after adding element with insert is : ', arr_3)

print('Array arr_3 element count of 102 is  : ', arr_3.count(102))

arr_3.append(1002)
arr_3.append(1003)

print('Array arr_3 after adding element with append is : ', arr_3)
# arr_3.extend(1001) # TypeError: 'int' object is not iterable
# print('Array arr_3 after adding element with append is : ', arr_3.itemsize(1001))
# TypeError: 'int' object is not callable

# Retrieve elements from array
print(".................Retrieval of element in array...............................")
print("Array elements arr_3: ", arr_3)

print("Array elements arr_3[0]: ", arr_3[0])

print("Array element arr_3[3]: ", arr_3[3])

print("Array element arr_3[3: 5]: ", arr_3[3: 5])

# https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/
print("...............Difference between List and Array in Python....................")

"""
List: A list in Python is a collection of items which can contain elements of multiple data types, which may be either 
numeric, character logical values, etc. It is an ordered collection supporting negative indexing. A list can be created
using [] containing data values.
Contents of lists can be easily merged and copied using python’s inbuilt functions.

"""
# creating a list containing elements
# belonging to different data types
sample_list = [1, "Ali", ['a', 'e']]
print("List : ", sample_list)

"""
Array: An array is a vector containing homogeneous elements i.e. belonging to the same data type. Elements are 
allocated with contiguous memory locations allowing easy modification, that is, addition, deletion, accessing of
 elements. In Python, we have to use the array module to declare arrays. If the elements of an array belong to 
 different data types, an exception “Incompatible data types” is thrown.

"""

# creating an array containing same
# data type elements

sample_array = ar.array('i', [1, 2, 3])
print("Array : ")
# accessing elements of array
for i in sample_array:
    print(i)

sample_array = ar.array('i', (1, 2, 3, 4, 5))
print("Array : ")
# accessing elements of array
for i in sample_array:
    print(i)

sample_array = ar.array('i', {1, 2, 3, 4, 5, 6, 7})
print("Array : ")
# accessing elements of array
for i in sample_array:
    print(i)
